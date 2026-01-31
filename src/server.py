#!/usr/bin/env python3
import socket
import threading

"""
Servidor de Estacionamento (Problema Leitores/Escritores)
Disciplina: Sistemas Operacionais
"""

# Configurações do Servidor
HOST = '127.0.0.1'
PORT = 65432
TOTAL_VAGAS = 10

# Estado compartilhado
vagas_disponiveis = TOTAL_VAGAS
# Lock para garantir exclusão mútua na escrita (modificação de vagas)
vaga_lock = threading.Lock()

def processar_cliente(conn, addr):
    """
    Função executada em thread separada para cada cliente conectado.
    """
    global vagas_disponiveis
    print(f"[NOVA CONEXÃO] Cliente {addr} conectado.")

    try:
        while True:
            # Recebe dados do cliente (buffer de 1024 bytes)
            data = conn.recv(1024)
            if not data:
                break
            
            mensagem = data.decode('utf-8').strip()
            resposta = ""

            # --- REGIÃO CRÍTICA (Início) ---
            # O Lock garante que apenas uma thread manipule o contador por vez
            with vaga_lock:
                if mensagem == 'consultar_vaga':
                    # Leitura: Retorna o estado atual
                    resposta = f"{vagas_disponiveis}"
                
                elif mensagem == 'pegar_vaga':
                    # Escrita: Modifica o estado se possível
                    if vagas_disponiveis > 0:
                        vagas_disponiveis -= 1
                        resposta = "SUCESSO"
                        print(f"[ESCRITA] Vaga ocupada por {addr}. Restam: {vagas_disponiveis}")
                    else:
                        resposta = "CHEIO"
                
                elif mensagem == 'liberar_vaga':
                    # Escrita: Modifica o estado
                    if vagas_disponiveis < TOTAL_VAGAS:
                        vagas_disponiveis += 1
                        resposta = "LIBERADA"
                        print(f"[ESCRITA] Vaga liberada por {addr}. Restam: {vagas_disponiveis}")
                    else:
                        resposta = "ERRO_JA_VAZIO"
                
                else:
                    resposta = "COMANDO_INVALIDO"
            # --- REGIÃO CRÍTICA (Fim) ---

            conn.sendall(resposta.encode('utf-8'))

    except Exception as e:
        print(f"[ERRO] Erro na conexão com {addr}: {e}")
    finally:
        conn.close()
        # print(f"[DESCONEXÃO] Cliente {addr} desconectou.")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    
    print(f"[*] Servidor ouvindo em {HOST}:{PORT}")
    print(f"[*] Vagas iniciais: {TOTAL_VAGAS}")

    try:
        while True:
            conn, addr = server.accept()
            # Cria uma thread para cada cliente (Simultaneidade)
            thread = threading.Thread(target=processar_cliente, args=(conn, addr))
            thread.start()
            print(f"[ATIVO] Conexões ativas: {threading.active_count() - 1}")
    except KeyboardInterrupt:
        print("\n[*] Desligando servidor...")
    finally:
        server.close()

if __name__ == "__main__":
    main()