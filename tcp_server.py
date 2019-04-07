# Servidor TCP
# Dev. por Anderson Garrote
# Adaptado de https://wiki.python.org.br/SocketBasico
# RA 743505

FILE_NAME = "serverFile.txt"

import time
import socket
import os
import sys

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

print "Servidor ouvindo na porta: ", PORT

while True:
    con, cliente = tcp.accept()
    pid = os.fork()
    if pid == 0:
        tcp.close()
        print 'Conectado por', cliente
        #Recebendo modo de operacao do cliente
        op = con.recv(1024)
        if op=='1':
            #Receber arquivo
            arq = open(FILE_NAME,'w')
            arq.write("");
            while True:
                msg = con.recv(1024)
                if not msg: break
                else: arq.write(msg)
            arq.close()
        else:
            #Enviar arquivo
            arq = open(FILE_NAME,'r')
            tcp.send (arq)
            arq.close()

        print 'Finalizando conexao do cliente', cliente
        con.close()
        sys.exit(0)
    else:
        con.close()
