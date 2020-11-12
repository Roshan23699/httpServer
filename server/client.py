from socket import *
def getClient():
	serverName = '127.0.0.1'
	serverPort = 12000
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName,serverPort))
	return clientSocket
def endClient(clientSocket):
	clientSocket.close()