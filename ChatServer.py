from socket import * 
serverPort = 12000 
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('',serverPort)) 
serverSocket.listen(1) 
connectionSocket, addr = serverSocket.accept()
print('The server is ready to receive\n To exit()') 
while True:
    sentence = connectionSocket.recv(1024).decode() 
    if sentence =='exit()':
    	print('Client has disconnected')
    	break
    else:
    	print('Client sent this', sentence)
    	message = input("what do you want to send")
    	if message == 'exit()':
    		connectionSocket.send(message.encode())
    		break
    	else:
    		connectionSocket.send(message.encode())
    		continue

serverSocket.close()