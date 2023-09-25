from socket import *
import threading
import random
import json

def clientHandeler(cennectionSocket, addr):
   print(str(addr) + ": has connected")
   while True:
      JsonRecived = cennectionSocket.recv(1024)
      JsonDict = json.loads(JsonRecived.decode())
      if (JsonDict == "##close##"):
         break
      if ( str(JsonDict.get('function')) == 'random'):
         if (int(JsonDict['num1']) > int(JsonDict['num2'])):
           ServerAwnser = random.randint(int(JsonDict['num2']),int(JsonDict['num1']) )
         else:
            ServerAwnser = random.randint(int(JsonDict['num1']),int(JsonDict['num2']) )
      elif (str(JsonDict.get('function')) == 'add'):
         ServerAwnser = int(JsonDict['num1']) + int(JsonDict['num2'])
      elif (str(JsonDict.get('function')) == 'subtract'):
         ServerAwnser = int(JsonDict['num1']) - int(JsonDict['num2'])
      else:
         ServerAwnser = "operation failed :(  "
      print(str(ServerAwnser) + " was send to: " + str(addr))
      JsonAwnser = json.dumps(ServerAwnser)
      cennectionSocket.send(JsonAwnser.encode())
   cennectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is up and ready')

while True:
   cennectionSocket, addr = serverSocket.accept()
   threading.Thread(target=clientHandeler, args=(cennectionSocket, addr)).start()
