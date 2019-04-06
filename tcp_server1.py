import time

def cliente_tcp():
  print("Hello from a function")
  pass

for i in range(1,4):

 start = time.time()

 #Execução
 cliente_tcp()

 stop = time.time()

 print("Execução TCP " + str(i) + ":")
 print(stop-start)

 pass
