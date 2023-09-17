from socket import *
import json

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
runTime = 0

while runTime <= 2:
   function = input('random, add, subtract: \n')
   num1 = input('number 1: \n')
   num2 = input('number 2: \n')
   Dictionary ={
      "function": function.strip(),
      "num1": num1.strip(),
      "num2": num2.strip(),
   }
   JsonDict = json.dumps(Dictionary)
   clientSocket.sendall(JsonDict.encode())
   modifiedSentence = clientSocket.recv(1024)
   FromServer = json.loads(modifiedSentence)
   print('From server: ', FromServer)
   runTime = runTime + 1
print("clossing connection")
closeCode = "##close##"
clientSocket.send(json.dumps(closeCode).encode())