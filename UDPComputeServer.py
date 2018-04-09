from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("The server is ready to receive")
while True:
	message1, clientAddress = serverSocket.recvfrom(2048)
	message2, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage1 = message1.decode()
	modifiedMessage2 = message2.decode()
	m2 = int(modifiedMessage1)
	m3 = int(modifiedMessage2)
	m4 = m2 + m3	
	m1 = str(m4)
	serverSocket.sendto(m1.encode(), clientAddress)
