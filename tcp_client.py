# Cliente TCP
# Dev. por Anderson Garrote
# RA 743505

import time
import socket

HOST = '192.168.1.10'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

def client_tcp():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    print("Para sair use CTRL+X\n")
    msg = raw_input()
    while msg != '\x18':
        tcp.send (msg)
        msg = raw_input()
    tcp.close()

for i in range(1,4):
    #Iniciando contador
    start = time.time()

    #Execução
    client_tcp()

    #Parando contador
    stop = time.time()

    #Exibindo resultado
    print("Execução TCP " + str(i) + ":")
    print(stop-start)

pass
