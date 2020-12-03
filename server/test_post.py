from tests import test_POST
import requests
from  time import time
from threading import Thread
import sys
import unittest
import os
from socket import *
from client import getClient, endClient

class Test_POST(unittest.TestCase):
	def test_status_code(self):
		clientSocket = getClient()
		sentence = "POST /lib.html \r\n\r\nname=roshan"
		clientSocket.send(sentence.encode())
		response = clientSocket.recv(1024)
		response = response.decode()
		file = 'testing/post/post200.txt'
		f = open(file, 'a')
		f.write(response)
		f.close()
		response = response.split(' ')
		status_code = response[1]
		self.assertEqual(int(status_code), 200)
		endClient(clientSocket)
		#the request from browser

	
	def test_complex_post(self):
		clientSocket = getClient()
		sentence = "POST /lib.html HTTP/1.1\r\nHost: 127.0.0.1:12000\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.8) Gecko/20100101 Firefox/60.8\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\nname=Roshan"
		clientSocket.send(sentence.encode())
		response = clientSocket.recv(1024)
		response = response.decode()
		file = 'testing/head/head200.txt'
		f = open(file, 'a')
		f.write(response)
		response = response.split(' ')
		f.close()
		status_code = response[1]
		self.assertEqual(int(status_code), 200)
		endClient(clientSocket)
if __name__ == "__main__":
	time = test_POST(int(50))
	print(time)
	unittest.main()
	os._exit(0)