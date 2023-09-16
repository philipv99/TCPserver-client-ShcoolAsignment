from socket import *

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
runTime = 0

while runTime <= 2:
   print("(Operations: random, add, subtract) \ntype 1 operation then 2 numbers seperated by';'")
   sentence = input('input a santence: \n')
   clientSocket.send(sentence.encode())
   modifiedSentence = clientSocket.recv(1024)
   print('From server: ', modifiedSentence.decode())
   runTime = runTime + 1
print("clossing connection")
clientSocket.send("##CloseLoop##".encode())
