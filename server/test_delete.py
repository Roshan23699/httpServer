from tests import test_DELETE
import requests
from  time import time
from threading import Thread
import sys
import unittest
import os
from socket import *
from client import getClient, endClient

class Test_DELETE(unittest.TestCase):

	def test_status_code(self):
		clientSocket = getClient()
		sentence = "DELETE /post/form.html \r\n\r\n"
		clientSocket.send(sentence.encode())
		response = clientSocket.recv(1024)
		response = response.decode()
		file = 'testing/delete/delete401.txt'
		f = open(file, 'a')
		f.write(response)
		f.close()
		response = response.split(' ')
		status_code = response[1]
		self.assertEqual(int(status_code), 401)
		endClient(clientSocket)

	def test_status_code_200(self):
		clientSocket = getClient()
		sentence = "DELETE /adminpermission/permission.html\r\nAuthorization: Basic YWJjOmFiYw==\r\n\r\nname=roshanbangar"
		clientSocket.send(sentence.encode())
		response = clientSocket.recv(1024)
		response = response.decode()
		file = 'testing/delete/delete200.txt'
		f = open(file, 'a')
		f.write(response)
		f.close()
		response = response.split(' ')
		status_code = response[1]
		self.assertEqual(int(status_code), 200)
		endClient(clientSocket)
		#the request from browser

	def test_status_code_202(self):
		clientSocket = getClient()
		sentence = "DELETE /volim/index.html\r\nAuthorization: Basic YWJjOmFiYw==\r\n\r\nname=roshanbangar"
		clientSocket.send(sentence.encode())
		response = clientSocket.recv(1024)
		response = response.decode()
		file = 'testing/delete/delete202.txt'
		f = open(file, 'a')
		f.write(response)
		f.close()
		response = response.split(' ')
		status_code = response[1]
		self.assertEqual(int(status_code), 202)
		endClient(clientSocket)
		#the request from browser

if __name__ == "__main__":
	time = test_DELETE(int(10))
	print(time)
	unittest.main()
	os._exit(0)