# Relatório: Problema Leitores/Escritores com Sockets

**Disciplina:** Sistemas Operacionais  
**Semestre:** 2025.2  
**Avaliação:** 5ª atividade avaliativa  
**Tecnologia:** Python com Sockets e Threads  

## Contexto inicial do trabalho (introdução)

O **Problema dos Leitores e Escritores** modela o acesso a um recurso compartilhado (como um banco de dados ou, neste caso, um contador de vagas de estacionamento) onde múltiplas threads podem ler o estado simultaneamente, mas a escrita exige acesso exclusivo.

Neste projeto, o cenário é um sistema distribuído cliente-servidor:
* **Recurso:** Um contador de vagas (iniciado em 10).
* **Leitores:** Clientes enviando `consultar_vaga`.
* **Escritores:** Clientes enviando `pegar_vaga` ou `liberar_vaga`.

O desafio principal é garantir a **consistência dos dados** (evitar que dois carros peguem a mesma vaga) num ambiente de rede.



## Descrevendo a solução em python para o problema de leitor / escritor

### Implementando o servidor e cliente

A solução utiliza a arquitetura TCP/IP via biblioteca `socket`:

1.  **Servidor (`server.py`):**
    * Atua como o guardião do estado (memória compartilhada).
    * Utiliza `threading` para aceitar múltiplas conexões simultâneas (até 50 clientes concorrentes).
    * Mantém uma variável global `vagas_disponiveis`.

2.  **Cliente (`client.py`):**
    * Simula 50 carros (threads) que tentam estacionar.
    * O cliente conecta, consulta, decide se tenta entrar, aguarda e sai.

## Tratando impasse (Deadlock)

### Qual a estratégia de tratamento de impasses

Embora o protocolo seja simples, problemas de concorrência podem ocorrer. A principal estratégia utilizada aqui foi o uso de **Exclusão Mútua com Granularidade Fina e Liberação Garantida**.

Para evitar inconsistências (Condição de Corrida) e Impasses:
1.  **Exclusão Mútua (Mutex):** Utilizamos um `threading.Lock` no servidor. Apenas uma thread pode alterar ou ler a variável `vagas_disponiveis` por vez.
2.  **Prevenção de Deadlock:**
    * **Lock Context Manager (`with lock:`):** O Python garante que, se ocorrer um erro dentro do bloco do lock, ele será liberado automaticamente. Isso evita que o servidor trave se uma thread falhar enquanto segura o recurso.
    * **Não-Bloqueio de Rede:** O lock protege *apenas* a operação na memória (rápida), não a comunicação de rede (lenta). O servidor não fica esperando resposta do cliente enquanto segura o lock.

### Implementação do tratamento de impasse em python

No arquivo `server.py`, a lógica de proteção é implementada assim:

```python
# Lock global criado no início
vaga_lock = threading.Lock()

# Dentro da thread de atendimento ao cliente
with vaga_lock:  # Adquire o lock -> Protege -> Libera automaticamente ao sair
    if mensagem == 'pegar_vaga':
        if vagas_disponiveis > 0:
            vagas_disponiveis -= 1
            resposta = "SUCESSO"
        else:
            resposta = "CHEIO"