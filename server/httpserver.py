from socket import *
import sys
import os
import datetime
from configparser import ConfigParser
from request_GET import request_GET
from support_functions import *
from request_HEAD import request_HEAD
from request_DELETE import request_DEL
from request_POST import *
from status_5XX import *
from support_functions import *
import pprint
import threading
import time
import re
#Global Section

parser = config_parser()


def response(client, addr, parser):
    requests = []
    msg = client.recv(1024).decode('utf-8')

    requests.append(msg)
    headers = check_header(str(msg))
    if headers:
        headers['method'] = str(msg).split()[0]
        headers['request-uri'] = str(msg).split()[1]
        headers['version'] = str(msg).split()[2]
        pprint.pprint(headers, width=160)
    else:
        headers['method'] = str(msg).split()[0]
        headers['request-uri'] = str(msg).split()[1]
        headers['version'] = str(msg).split()[2]
        pprint.pprint(headers, width=160)
    request(client, addr, parser, headers, msg)
    return
        # if msg == '\r\n':
        #     #print("hi")
        #     request(client, addr, parser, requests)
        #     return
        # requests.append(msg)

def timeout(client, addr, parser): 
    dict1 = ''
    path = parser.get('server', 'DocumentRoot')
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


def request(client, addr, parser, headers, msg):
    if(len(headers) == 0):
        return
    if headers['method'] == "GET":
        request_GET(headers, client, addr, parser)
    elif headers['method'] == "POST":
        request_POST(headers, client, addr, parser, msg)
    elif headers['method'] == "HEAD":
        request_HEAD(headers1, client, addr, parser)
    elif headers['method'] == "DELETE":
        request_DEL(headers1,client, addr,parser)
    elif headers['method'] == "PUT":
        request_PUT(headers1, client, addr, parser)
    else:
        not_implemented(headers1, client, addr, parser)
        
if __name__ == "__main__":
    host = '127.0.0.1'
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    port = int(sys.argv[1])
    server_socket.bind(('', port))
    server_socket.listen(1)
    print("Server is ready to listen")


    while True:
        client, addr = server_socket.accept()
        print("connection has recieved from ip", addr[0])
        print("on port", addr[1])
        # requests = []
        # msg = client.recv(1024).decode('utf-8')
        # requests.append(msg)
        # request(client, addr, parser, requests)
        try:
            new_client = threading.Thread(target=response, args=[client, addr, parser])
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
        #     request_GET(dict1, client, addr, parser)
