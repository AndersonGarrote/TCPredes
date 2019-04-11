# Servidor UDP
# Dev. por Anderson Garrote
# Adaptado de https://wiki.python.org.br/SocketBasico
#   e https://gist.github.com/giefko/2fa22e01ff98e72a5be2
# RA 743505

FILE_NAME = "serverFileUDP.txt"
import socket
import sys
import select

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

def conectado(con):

    while True:
        #Recebendo modo de operacao cliente
        op, cliente = con.recvfrom(1024)

        if op=="2":
            #Enviar arquivo
            arq = open(FILE_NAME,'r+')
            print("Enviando arquivo...")
            buffer = arq.read(1024)
            while buffer:
                con.sendto(buffer,dest)
                buffer = con.read(1024)
                pass
            con.send(buffer)
            arq.close()
            print("Arquivo enviado!")
            print('Finalizando conexao com o cliente', cliente)
            con.close()

        elif op=="1":
            #Receber arquivo
            arq = open(FILE_NAME,'w+')
            print("Recebendo arquivo...")
            try:
                while True:
                    con.settimeout(2)
                    buffer, cliente = con.recvfrom(1024)
                    arq.write(buffer)
            except timeout:
                arq.close()
                print("Arquivo recebido!")
                print('Finalizando conexao com o cliente', cliente)
                con.close()

def main():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    orig = (HOST, PORT)

    udp.bind(orig)

    conectado(udp)

if __name__ == '__main__':
    main()
