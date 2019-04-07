# Cliente TCP
# Dev. por Anderson Garrote
# RA 743505

import time
import socket

HOST = '192.168.10.106'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
FILE_NAME = '1mb'

def client_tcp(op):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    #Enviando modo de operacao ao servidor
    tcp.send (op)

    if op=='1':
        #Enviar arquivo
        arq = open(FILE_NAME+".txt",'r')
        tcp.send (arq)
        arq.close()
    else:
        #Receber arquivo
        arq = open(FILE_NAME+"_new.txt",'w')
        while True:
            msg = con.recv(1024)
            if not msg: break
            else: arq.write(msg)
        arq.close()
    tcp.close()

def main():
    for i in range(1,4):
        #Iniciando contador
        start = time.time()

        op=input("Selecione um modo de operacao:")
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
