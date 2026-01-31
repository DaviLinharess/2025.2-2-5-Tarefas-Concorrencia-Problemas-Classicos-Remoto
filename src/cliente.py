#!/usr/bin/env python3
import socket
import threading
import time
import random

"""
Cliente (Simulação de Carros)
"""

HOST = '127.0.0.1'
PORT = 65432
NUM_CLIENTES = 50

class Cliente(threading.Thread):
    def __init__(self, cliente_id):
        super().__init__()
        self.cliente_id = cliente_id

    def enviar_mensagem(self, sock, mensagem):
        sock.sendall(mensagem.encode('utf-8'))
        dados = sock.recv(1024)
        return dados.decode('utf-8')

    def run(self):
        """
        Ciclo de vida do cliente:
        1. Conecta
        2. Consulta vaga (Leitura)
        3. Se tiver vaga, tenta pegar (Escrita)
        4. Fica estacionado (Sleep)
        5. Libera vaga (Escrita)
        6. Desconecta
        """
        try:
            # Simula tempo aleatório de chegada
            time.sleep(random.uniform(0, 2))
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            
            # 1. Consultar Vagas (Leitor)
            resp_vagas = self.enviar_mensagem(sock, 'consultar_vaga')
            vagas = int(resp_vagas)
            
            print(f"[Carro {self.cliente_id}] consultou. Vagas disponíveis: {vagas}")
            
            if vagas > 0:
                # Tenta pegar a vaga (Escritor)
                resp_pegar = self.enviar_mensagem(sock, 'pegar_vaga')
                
                if resp_pegar == "SUCESSO":
                    print(f"🟢 [Carro {self.cliente_id}] ESTACIONOU.")
                    
                    # Simula tempo estacionado
                    tempo_estacionado = random.uniform(1, 3)
                    time.sleep(tempo_estacionado)
                    
                    # Libera a vaga (Escritor)
                    self.enviar_mensagem(sock, 'liberar_vaga')
                    print(f"🔴 [Carro {self.cliente_id}] SAIU do estacionamento.")
                else:
                    print(f"⚠️ [Carro {self.cliente_id}] TENTOU mas estava CHEIO na hora do click.")
            else:
                print(f"⛔ [Carro {self.cliente_id}] DESISTIU (Estacionamento Cheio).")
                
            sock.close()
            
        except Exception as e:
            print(f"[Carro {self.cliente_id}] Erro: {e}")

def main():
    print(f"Iniciando simulação com {NUM_CLIENTES} carros...")
    clientes = []
    
    # Cria as threads dos clientes
    for i in range(NUM_CLIENTES):
        c = Cliente(i)
        clientes.append(c)
        c.start()
        
    # Aguarda todos terminarem
    for c in clientes:
        c.join()
        
    print("Simulação finalizada.")

if __name__ == "__main__":
    main()