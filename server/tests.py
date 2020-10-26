import requests
from  time import time
from threading import Thread
import sys
def test_GET(no_of_requests_at_a_time):
	url = 'http://127.0.0.1:12000/volim/'
	start = time()
	for _ in range(no_of_requests_at_a_time):
		new_thread = Thread(target=send_GET, args=[url, ])
		new_thread.start()
	end = time()
	return end - start


def send_GET(url):
	r = requests.get(url)
	r.close()

if __name__ == "__main__":
	time = test_GET(300)
	print(time)
	sys.exit(0)
	