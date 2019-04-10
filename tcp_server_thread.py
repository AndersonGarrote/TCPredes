# Servidor TCP
# Dev. por Anderson Garrote
# Adaptado de https://wiki.python.org.br/SocketBasico
#   e https://gist.github.com/giefko/2fa22e01ff98e72a5be2
# RA 743505

FILE_NAME = "serverFile.txt"
import socket
import thread

HOST = ''              # Endereco IP do Servidor
PORT = 50001            # Porta que o Servidor esta

def conectado(con, cliente):
    print('Conectado por', cliente)

    while True:
        #Recebendo modo de operacao cliente
        op=con.recv(2)

        if op=="2":
            #Enviar arquivo
            arq = open(FILE_NAME,'r+')
            print("Enviando arquivo...")
            buffer = arq.read(1024)
            while buffer:
                con.send(buffer)
                buffer = arq.read(1024)
                pass
            con.send("")
            arq.close()
            print("Arquivo enviado!")
        elif op=="1":
            #Receber arquivo
            arq = open(FILE_NAME,'w+')
            print("Recebendo arquivo...")
            while True:
                buffer = con.recv(1024)
                if not buffer: break
                else: arq.write(buffer)
            arq.close()
            print("Arquivo recebido!")

    print('Finalizando conexao com o cliente', cliente)
    con.close()
    thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(5)

while True:
    con, cliente = tcp.accept()
    thread.start_new_thread(conectado, tuple([con, cliente]))
