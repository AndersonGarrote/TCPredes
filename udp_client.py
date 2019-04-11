# Cliente UDP
# Dev. por Anderson Garrote
# Adaptado de https://wiki.python.org.br/SocketBasico
#   e https://gist.github.com/giefko/2fa22e01ff98e72a5be2
# RA 743505

import time
import socket

HOST = 'localhost'#'200.9.84.163'  # Endereco IP do Servidor
PORT = 5000                        # Porta que o Servidor esta
FILE_NAME = '5mb'

def client_udp(op):
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)

    #Enviando modo de operacao ao servidor
    udp.sendto(str(op),dest)
    if op==1:
        #Enviar arquivo
        arq = open(FILE_NAME+".txt",'r+')

        print("Enviando arquivo...")
        buffer = arq.read(1024)
        while buffer:
            udp.sendto(buffer,dest)
            buffer = arq.read(1024)
            pass
        udp.sendto(buffer,dest)
        arq.close()
        print("Arquivo enviado!")
        udp.close()
    elif op==2:
        print("Recebendo arquivo...")
        #Receber arquivo
        arq = open(FILE_NAME+"_new.txt",'wb+')
        while True:
            buffer, servidor = udp.recvfrom(1024)
            if not buffer: break
            arq.write(buffer)
        arq.close()
        print("Arquivo recebido!")
        udp.close()
    else:
        return
def main():
    for i in range(1,4):

        op=input("Selecione um modo de operacao:")

        #Iniciando contador
        start = time.time()

        #Execucao
        client_udp(op)

        #Parando contador
        stop = time.time()

        #Exibindo resultado
        print("Execucao UDP " + str(i) + ":")
        print(stop-start)

    pass

if __name__ == '__main__':
    main()
