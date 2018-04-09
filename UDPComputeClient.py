from socket import *

print('Enter Hours')
first = input()
print('Enter Rate')
second= input()


#NETWORK
serverName = '10.0.2.15'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message1 = first
message2 = second
clientSocket.sendto(message1.encode(), (serverName, serverPort))
clientSocket.sendto(message2.encode(), (serverName, serverPort))
m1, serverAddress = clientSocket.recvfrom(2048)
print(m1.decode())
