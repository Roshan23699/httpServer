import requests
from  time import time
from threading import Thread
import sys
import unittest
import os
#stress test
def test_GET(no_of_requests_at_a_time):

	data = {'somekey': 'somevalue'}
	start = time()
	url = 'http://127.0.0.1:12000/lib.html'
	for _ in range(no_of_requests_at_a_time):
		new_thread = Thread(target=send_GET, args=[url, ])
		new_thread.start()
	end = time()
	return end - start

def test_HEAD(no_of_requests_at_a_time):
	url = 'http://127.0.0.1:12000/lib.html'
	data = {'somekey': 'somevalue'}
	t1 = time()
	for _ in range(no_of_requests_at_a_time):
		new_thread = Thread(target=send_HEAD, args=[url, ])
		new_thread.start()
	t2 = time()
	return t2 - t1


#stress test
def test_PUT(no_of_requests_at_a_time):
	url = 'http://127.0.0.1:12000/t.html'
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
	url = 'http://127.0.0.1:12000/post/form.html'
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




def send_GET(url):
	r = requests.get(url)
	r.close()
	sys.exit()


def send_POST(url, data):
	r = requests.post(url, data)
	r.close()
	sys.exit()

def send_DELETE(url):
	r = requests.delete(url)
	r.close()
	sys.exit()


def send_PUT(url, data):
	r = requests.put(url, data)
	r.close()
	sys.exit()


def send_HEAD(url):
	r = requests.head(url)
	r.close()
	sys.exit()





#for the stress test sending 50 requests each at one time
def stress_test(no_of_requests_at_a_time):
	data = {'somekey': 'somevalue'}
	url = 'http://127.0.0.1:12000/volim/'
	start = time()
	for _ in range(no_of_requests_at_a_time):
		new_thread = Thread(target=send_POST, args=[url, data, ])
		new_thread.start()

	for _ in range(no_of_requests_at_a_time):
		new_thread = Thread(target=send_PUT, args=[url, data, ])
		new_thread.start()

	url = 'http://127.0.0.1:12000/post/form.html'
	for _ in range(no_of_requests_at_a_time):
		new_thread = Thread(target=send_DELETE, args=[url, ])
		new_thread.start()
	url = 'http://127.0.0.1:12000/lib.html'
	for _ in range(no_of_requests_at_a_time):
		new_thread = Thread(target=send_GET, args=[url, ])
		new_thread.start()
	for _ in range(no_of_requests_at_a_time):
		new_thread = Thread(target=send_HEAD, args=[url, ])
		new_thread.start()
	end = time()
	return end - start

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
	# clientSocket.bind((1, clientSocket));
	#above commented lines resulted in error binding failed
	clientSocket.connect((serverName,serverPort))
	# sentence = raw_input('Input lowercase sentence:')
	# clientSocket.send(sentence.encode())
	# modifiedSentence = clientSocket.recv(1024)
	# print('From Server: ', modifiedSentence.decode())
	# clientSocket.close()

	# time = test_GET(100)
	# print('time for 100 get requests' + ' :' + str(time))
	time = test_HEAD(int(100))
	# print('time for 100 head requests' + ' :' + str(time))
	# time += test_PUT(50)
	# send_GET('http://127.0.0.1:12000/lib.html')
	# send_GET('http://127.0.0.1:12000/lib.html')
	# send_GET('http://127.0.0.1:12000/lib.html')
	# send_GET('http://127.0.0.1:12000/lib.html')
	data = {'somekey': 'somevalue'}
	# send_DELETE('http://127.0.0.1:12000/post/form.html')
	# time = test_DELETE(10)
	# time = stress_test(30)
	print(str(time))

	os._exit(0)
