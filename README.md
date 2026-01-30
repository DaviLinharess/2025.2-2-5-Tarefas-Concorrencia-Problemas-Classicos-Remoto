# Atividade avaliativa do 2o bimestre - Implementar solução para o Problema do leitores/escritores em python com sockets

## Contexto

- **Disciplina**: Sistemas operacionais
- **Semestre letivo**: 2025.2
- **Avaliação**: **5a** atividade avaliativa do bimestre
- **Time de desenvolvimento**: A solução do problema pode ser feita em grupo, com ou sem ajuda de assistente, mas a **entrega deve ser individual via fork desse repositório**.
- **Deadline**: 08/02/2026 com apresentação em 09/02/2026

## Descrição do Problema

O Problema do Leitores/Escritores é um problema clássico de concorrência que ilustra os desafios de diversas tarefas acessando de forma concorrente uma área de memória compartilhada para leituras ou escritas de valores.
As leituras podem ser feitas em simultaneamente mas as escritas têm de ser feitas com acesso exclusivo para evitar condições de disputa/inconsistência.
Exemplos de leitura e escrita em sistemas web: consulta de saldo/saque ou depósito; consulta de disponibilidade ingresso/compra de ingresso, consulta de estoque de produto/compra do produto em estoque.

## Requisitos da Implementação

1. ✅ Serão 10 vagas disponibilizadas
2. ✅ O processo `server.py` gerencia as 10 vagas através de um protocolo com as seguintes mensagens: 
   - `consultar_vaga`:  retorna o número de vagas disponíveis
   - `pegar_vaga`: pega uma vaga de estacionamento
   - `liberar_vaga`: libera uma vaga de estacionamento e sai do estacionamento
3. ✅ O processo `server.py` escuta clientes simultaneamente, usa `threads`
4. ✅ O processo `client.py` deve ter 50 clientes
   - o arquivo `cliente.py` esta praticamente vazio, contém classe e função main a serem preenchidos

## Entrega deve conter

1. Código fonte em python com as libs em requirements
2. Relatório no arquivo `relatorio.md` com a estrutura abaixo
   - Título
   - Contexto inicial do trabalho (introdução)
   - Descrevendo a solução em python para o problema de leitor / escritor
     - Implementando o servidor e cliente
     - Tratando impasse
       - Qual a estratégia de tratamento de impasses
       - Implementação do tratamento de impasse em python
   - Executar o código e descrever comportamento observado
   - Considerações finais

**Lembre**: 
- é necessário fazer fork desse repositório.
- o relatório pode conter imagens ou bloco de código para as saídas

## Conceitos de Concorrência Demonstrados nesse projeto

- **Sockets**: Comunicação entre tarefas usando sockets
- **Exclusão Mútua** remota: Uso de locks remotos para garantir acesso exclusivo aos recursos remotos
- **Sincronização**: Coordenação entre processos remotos sem comunicação direta
- **Prevenção de Deadlock**: Técnica de ordenação de recursos
- **Condição de Corrida**: Evitada através do uso adequado de locks remoto

## Código gerado pelo copilot para este trabalho

FIXME