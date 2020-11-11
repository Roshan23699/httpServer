import requests
from  time import time
from threading import Thread
import sys
#stress test
def test_GET(no_of_requests_at_a_time):
	url = 'http://127.0.0.1:12000/volim/index.html'
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

if __name__ == "__main__":
	test_HEAD(1)
	#time = test_GET(10)
	#print(time)
	sys.exit(0)
	