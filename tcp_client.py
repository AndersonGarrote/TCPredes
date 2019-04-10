# Cliente TCP
# Dev. por Anderson Garrote
# Adaptado de https://wiki.python.org.br/SocketBasico
#   e https://gist.github.com/giefko/2fa22e01ff98e72a5be2
# RA 743505

import time
import socket

HOST = '200.9.84.163'  # Endereco IP do Servidor
PORT = 50001            # Porta que o Servidor esta
FILE_NAME = '1mb'

def client_tcp():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)

    op=input("Selecione um modo de operacao:")
    #Enviando modo de operacao ao servidor
    tcp.send(str(op))
    if op==1:
        #Enviar arquivo
        arq = open(FILE_NAME+".txt",'r+')
        print("Enviando arquivo...")
        buffer = arq.read(1024)
        while buffer:
            tcp.send(buffer)
            buffer = arq.read(1024)
            pass
        arq.close()
        print("Arquivo enviado!")
    elif op==2:
        #Receber arquivo
        arq = open(FILE_NAME+"_new.txt",'w+')
        print("Recebendo arquivo...")
        while True:
            buffer = tcp.recv(1024)
            print(not buffer)
            if not buffer: break
            print('recebendo...')
            arq.write(buffer)
        arq.close()
        print("Arquivo recebido!")
    tcp.close()

def main():
    for i in range(1,4):
        #Iniciando contador
        start = time.time()

        #Execucao
        client_tcp()

        #Parando contador
        stop = time.time()

        #Exibindo resultado
        print("Execucao TCP " + str(i) + ":")
        print(stop-start)

    pass

if __name__ == '__main__':
    main()
