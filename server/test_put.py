from tests import test_PUT
import requests
from  time import time
from threading import Thread
import sys
import unittest
import os
from socket import *
from client import getClient, endClient

class Test_PUT(unittest.TestCase):
	#unauthorized request
	def test_status_code_401(self):
		clientSocket = getClient()
		sentence = "PUT /post/demo.txt \r\n\r\nname=roshan"
		clientSocket.send(sentence.encode())
		response = clientSocket.recv(1024)
		response = response.decode()
		file = 'testing/put/put401.txt'
		f = open(file, 'a')
		f.write(response)
		f.close()
		response = response.split(' ')
		status_code = response[1]
		self.assertEqual(int(status_code), 401)
		endClient(clientSocket)
		#the request from browser

	def test_status_code_200(self):
		clientSocket = getClient()
		sentence = "PUT /post/demo.txt\r\nAuthorization: Basic YWJjOmFiYw==\r\n\r\nname=roshanbangar"
		clientSocket.send(sentence.encode())
		response = clientSocket.recv(1024)
		response = response.decode()
		file = 'testing/put/put200.txt'
		f = open(file, 'a')
		f.write(response)
		f.close()
		response = response.split(' ')
		status_code = response[1]
		self.assertEqual(int(status_code), 200)
		endClient(clientSocket)
		#the request from browser

	def test_status_code_201(self):
		clientSocket = getClient()
		sentence = "PUT /post/demo4.txt\r\nAuthorization: Basic YWJjOmFiYw==\r\n\r\nname=roshan"
		clientSocket.send(sentence.encode())
		response = clientSocket.recv(1024)
		response = response.decode()
		file = 'testing/put/put201.txt'
		f = open(file, 'a')
		f.write(response)
		f.close()
		response = response.split(' ')
		status_code = response[1]
		self.assertEqual(int(status_code), 201)
		endClient(clientSocket)
		#the request from browser

	def test_status_code_204(self):
		clientSocket = getClient()
		sentence = "PUT /post/demo2.txt\r\nAuthorization: Basic YWJjOmFiYw==\r\n\r\nname=roshan"
		clientSocket.send(sentence.encode())
		response = clientSocket.recv(1024)
		response = response.decode()
		file = 'testing/put/put204.txt'
		f = open(file, 'a')
		f.write(response)
		f.close()
		response = response.split(' ')
		status_code = response[1]
		self.assertEqual(int(status_code), 204)
		endClient(clientSocket)
		#the request from browser
	
	
if __name__ == "__main__":
	unittest.main()