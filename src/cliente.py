#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cliente TCP para gerenciamento de vagas de estacionamento.
O cliente envia comandos ao servidor para consultar,
pegar e liberar vagas.

Autor: ChatGPT e Copilot com orientação e revisão de Minora
Data: 2024-06-15

Procure por FIXME para identificar pontos que precisam de implementação adicional.

"""

import threading
import socket
import os
from dotenv import load_dotenv


class ClienteEstacionamento(threading.Thread):
    def __init__(self, socket_cliente):
        threading.Thread.__init__(self)
        self.socket_cliente = socket_cliente

    def run(self):
        # Método de execução da thread.
        # FIXME: Implemente a lógica de tem vaga, estaciona, passeia e libera vaga
        pass

    def consultar_vaga(self):
        # Consulta a quantidade de vagas disponíveis no servidor.
        # FIXME: Implemente a lógica de consulta de vagas retornando true ou false
        pass

    def pegar_vaga(self):
        # Tenta pegar uma vaga no servidor.
        # FIXME: Implemente a lógica de pegar vaga de estacionamento retornando true ou false
        pass

    def liberar_vaga(self):
        # Libera a vaga ocupada no servidor.
        # FIXME: Implemente a lógica de liberar vaga de estacionamento retornando true ou false
        pass
    
    def passear(self):
        # Simula o tempo que o cliente fica com a vaga ocupada.
        # FIXME: Implemente a lógica de simulação de tempo de uso da vaga
        pass

def criar_socket_cliente():
    # Cria e retorna um socket TCP para o cliente.
    load_dotenv()
    PORTA = int(os.getenv('PORT', 5000))

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', PORTA))
    print('Conectado ao servidor de estacionamento')
    return cliente

def main():
    # Função principal para iniciar o cliente.
    # FIXME: Implemente a lógica para iniciar 50 clientes concorrentes
    # Lembre que são 50 clientes concorrentes
    # Código comentado abaixo é apenas um exemplo de como iniciar um cliente
    ### socket = criar_socket_cliente()
    ### cliente = ClienteEstacionamento(socket)
    ### cliente.start()
    pass

if __name__ == "__main__":
    main()