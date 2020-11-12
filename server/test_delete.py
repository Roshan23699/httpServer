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
	# def test_status_code_201(self):
	# 	clientSocket = getClient()
	# 	sentence = "PUT /post/demo.txt \r\n\r\nname=roshan"
	# 	clientSocket.send(sentence.encode())
	# 	response = clientSocket.recv(1024)
	# 	response = response.decode()
	# 	file = 'testing/put/put200.txt'
	# 	f = open(file, 'a')
	# 	f.write(response)
	# 	f.close()
	# 	response = response.split(' ')
	# 	status_code = response[1]
	# 	self.assertEqual(int(status_code), 201)
	# 	endClient(clientSocket)
	# 	#the request from browser

	def test_status_code(self):
		clientSocket = getClient()
		sentence = "DELETE /post/form.html \r\n\r\n"
		clientSocket.send(sentence.encode())
		response = clientSocket.recv(1024)
		response = response.decode()
		file = 'testing/delete/delete200.txt'
		f = open(file, 'a')
		f.write(response)
		f.close()
		response = response.split(' ')
		status_code = response[1]
		self.assertEqual(int(status_code), 401)
		endClient(clientSocket)
if __name__ == "__main__":
	# time = test_DELETE(int(10))
	# print(time)
	unittest.main()
	os._exit(0)