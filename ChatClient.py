#Network
from socket import *
serverName = 'serverName'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print('You are now connected\n To exit just type exit()\n')
while True:
	message = input('What do you want to send')
	if message == 'exit()':
		message = 'exit()'
		clientSocket.send(message.encode())
		break
	else:
		clientSocket.send(message.encode())
		modifiedSentence = clientSocket.recv(1024).decode()
		if modifiedSentence == 'exit()':
			print('User has disconnected')
			break
		else:
			print('From server :', modifiedSentence)
			continue

clientSocket.close()