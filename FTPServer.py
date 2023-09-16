from socket import *
import threading
import random

def clientHandeler(cennectionSocket, addr):
   print(str(addr) + ": has connected")
   while True:
      sentence = cennectionSocket.recv(1024).decode().strip()
      if (sentence == "##CloseLoop##"):
         break
      ServerSentence = sentence.lower()
      print("from client: " + sentence)
      ServerSentenceList = str(ServerSentence).split(";")
      if (ServerSentenceList[0] == "random"):
         ServerAwnser = random.randint(int(ServerSentenceList[1]),int(ServerSentenceList[2]) )
      elif (ServerSentenceList[0] == "add"):
         ServerAwnser = int(ServerSentenceList[1]) + int(ServerSentenceList[2])
      elif (ServerSentenceList[0] == "subtract"):
         ServerAwnser = int(ServerSentenceList[1]) - int(ServerSentenceList[2])
      else:
         ServerAwnser = "operation failed :(  "
      print(str(ServerAwnser) + " was send to: " + str(addr))
      cennectionSocket.send(str(ServerAwnser).encode())
   cennectionSocket.send("clossing clients".encode())
   cennectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is up and ready')

while True:
   cennectionSocket, addr = serverSocket.accept()
   threading.Thread(target=clientHandeler, args=(cennectionSocket, addr)).start()
