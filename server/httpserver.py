from socket import *
import sys
import os
import datetime
from request_GET import request_GET
from support_functions import *
from request_HEAD import request_HEAD
from request_DELETE import request_DEL
from request_POST import *

import threading
import time
import re
#Global Section
ROOT = "../var/www/html"

def response(client, addr, ROOT):
    requests = []
    msg = client.recv(1024).decode('utf-8')
    requests.append(msg)
    request(client, addr, ROOT, requests, msg)
    return
        # if msg == '\r\n':
        #     #print("hi")
        #     request(client, addr, ROOT, requests)
        #     return
        # requests.append(msg)

def timeout(client, addr, ROOT): 
    dict1 = ''
    path = ROOT
    path += "/error/timeout.html"
    content_type = check_extention(path)
    server_response = "HTTP/1.1 400 Request Timeout\n"
    curr_time = datetime.datetime.now()
    server_response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
    server_response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
    content_length = os.path.getsize(path)
    server_response += "Content-Length: " + str(content_length) + "\n"
    #response += "Connection: close\n"
    server_response += "Content-Type: text/html; charset=iso-8859-1\n\n"
    server_response  = server_response.encode()
    server_response += read_file(path, content_type)
    client.send(server_response)
    if find_value("Connection:", dict1) != "keep-alive":
        client.close()


def request(client, addr, ROOT, requests, msg):
    dict1 = requests[0].split()
    if(len(dict1) == 0):
        return
    if dict1[0] == "GET":
        request_GET(dict1, client, addr, ROOT)
    elif dict1[0] == "POST":
        request_POST(dict1, client, addr, ROOT, msg)
    elif dict1[0] == "HEAD":
        request_HEAD(dict1, client, addr, ROOT)
    elif dict1[0] == "DELETE":
        request_DEL(dict1,client, addr,ROOT)
        
if __name__ == "__main__":
    host = '127.0.0.1'
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    port = int(sys.argv[1])
    server_socket.bind(('', port))
    server_socket.listen(2)
    print("Server is ready to listen")


    while True:
        client, addr = server_socket.accept()
        print("connection has recieved from ip", addr[0])
        print("on port", addr[1])
        # requests = []
        # msg = client.recv(1024).decode('utf-8')
        # requests.append(msg)
        # request(client, addr, ROOT, requests)
        try:
            new_client = threading.Thread(target=response, args=[client, addr, ROOT])
            new_client.daemon = True
            new_client.start()
            #new_client.join()
        except Exception or OSError:
            print()
        # client.close()
        #msg = client.recv(1024).decode('utf-8')
        #while not (msg[len(msg) - 2] == '\n' and msg[len(msg) - 1] == '\n'):
            #msg += client.recv(1024).decode('utf-8')
            #print(msg)
        # dict1 = msg.split()
        # if len(dict1) == 0:
        #     continue
        # print(dict1)
        
        # #check for the request
        # if dict1[0] == "GET":
        #     request_GET(dict1, client, addr, ROOT)
