# Cliente TCP
# Dev. por Anderson Garrote
# Adaptado de https://wiki.python.org.br/SocketBasico
#   e https://gist.github.com/giefko/2fa22e01ff98e72a5be2
# RA 743505

import time
import socket
import os

HOST = 'localhost'#'200.9.84.163'  # Endereco IP do Servidor
PORT = 5000                        # Porta que o Servidor esta
FILE_NAME = '1mb'

def client_tcp(op):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    #Enviando modo de operacao ao servidor
    tcp.sendall(str(op))
    print(tcp.recv(1024))
    if op==1:
        #Enviar arquivo
        arq = open(FILE_NAME+".txt",'r+')

        print("Enviando arquivo...")
        buffer = arq.read(1024)
        while buffer:
            tcp.sendall(buffer)
            buffer = arq.read(1024)
            pass
        arq.close()
        print("Arquivo enviado!")
    elif op==2:
        print("Recebendo arquivo...")
        while True:
            #Receber arquivo
            arq = open(FILE_NAME+"_new.txt",'wb+')
            buffer = tcp.recv(1024)
            if not buffer: break
            arq.write(buffer)
            arq.close()
        print("Arquivo recebido!")

    tcp.close()

def main():
    for i in range(1,4):

        op=input("Selecione um modo de operacao:")
        #Iniciando contador
        start = time.time()

        #Execucao
        client_tcp(op)

        #Parando contador
        stop = time.time()

        #Exibindo resultado
        print("Execucao TCP " + str(i) + ":")
        print(stop-start)

    pass

if __name__ == '__main__':
    main()
