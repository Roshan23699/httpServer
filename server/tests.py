import requests
from  time import time
from threading import Thread
import sys
import unittest
#stress test
def test_GET(no_of_requests_at_a_time):
	url = 'http://127.0.0.1:12000/volim/'
	data = {'somekey': 'somevalue'}
	start = time()
	for _ in range(no_of_requests_at_a_time):
		new_thread = Thread(target=send_GET, args=[url, ])
		new_thread.start()
	end = time()
	return end - start


#stress test
def test_PUT(no_of_requests_at_a_time):
	url = 'http://127.0.0.1:12000/volim/'
	data = {'somekey': 'somevalue'}
	start = time()
	for _ in range(no_of_requests_at_a_time):
		new_thread = Thread(target=send_PUT, args=[url, data, ])
		new_thread.start()
	end = time()
	return end - start


#stress test
def test_DELETE(no_of_requests_at_a_time):
	data = {'somekey': 'somevalue'}
	url = 'http://127.0.0.1:12000/volim/'
	start = time()
	for _ in range(no_of_requests_at_a_time):
		new_thread = Thread(target=send_DELETE, args=[url, ])
		new_thread.start()
	end = time()
	return end - start

def test_POST(no_of_requests_at_a_time):
	data = {'somekey': 'somevalue'}
	url = 'http://127.0.0.1:12000/volim/'
	start = time()
	for _ in range(no_of_requests_at_a_time):
		new_thread = Thread(target=send_POST, args=[url, data, ])
		new_thread.start()
	end = time()
	return end - start

def test_HEAD(no_of_requests_at_a_time):
	data = {'somekey': 'somevalue'}
	url = 'http://127.0.0.1:12000/volim/index.html'
	start = time()
	for _ in range(no_of_requests_at_a_time):
		new_thread = Thread(target=send_HEAD, args=[url, ])
		new_thread.start()
	end = time()
	return end - start



def send_GET(url):
	r = requests.get(url)
	r.close()


def send_POST(url, data):
	r = requests.post(url, data)
	r.close()

def send_DELETE(url):
	r = requests.delete(url)
	r.close()


def send_PUT(url, data):
	r = requests.put(url, data)
	r.close()


def send_HEAD(url):
	r = requests.head(url)
	r.close()






#confirmance tests
class Test_GET(unittest.TestCase):
	def test_status_code(self, clientSocket):
		
		pass


if __name__ == "__main__":
	#client for confirmance tests
	from socket import *
	serverName = '127.0.0.1'
	serverPort = 12000
	#clientPort = 12004
	clientSocket = socket(AF_INET, SOCK_STREAM)
	#clientSocket.bind((1, clientSocket));
	#above commented lines resulted in error binding failed
	clientSocket.connect((serverName,serverPort))
	# sentence = raw_input('Input lowercase sentence:')
	# clientSocket.send(sentence.encode())
	# modifiedSentence = clientSocket.recv(1024)
	# print('From Server: ', modifiedSentence.decode())
	# clientSocket.close()
	time = test_GET(300)
	print(time)
	sys.exit(0)
	