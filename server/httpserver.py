from socket import *
import sys
import os
import datetime
from configparser import ConfigParser
from request_GET import request_GET
from request_HEAD import request_HEAD
from request_DELETE import request_DEL
from request_POST import *
from status_5XX import *
from status_4XX import *
from support_functions import *
from request_PUT import *
from log_functions import *
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
    if(len(msg) == 0):
        return
    headers = check_header(str(msg))
    firstline = str(msg).split('\r\n')
    if firstline[0].split():
        headers['method'] = firstline[0].split()[0]
        headers['request-uri'] = firstline[0].split()[1]
        if len(firstline[0].split()) > 2:
            headers['version'] = firstline[0].split()[2]
    else:
        bad_request(headers, client, addr, parser)

    pprint.pprint(headers, width=160)
    request(client, addr, parser, headers, msg)
    return
   
def timeout(client, addr, parser): 
    time.sleep(10)
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
    client.close()


def request(client, addr, parser, headers, msg):
    if headers is None:
        return
    if headers['method'] == "GET":
        request_GET(headers, client, addr, parser)
    elif headers['method'] == "POST":
        request_POST(headers, client, addr, parser, msg)
    elif headers['method'] == "HEAD":
        request_HEAD(headers, client, addr, parser)
    elif headers['method'] == "DELETE":
        request_DEL(headers,client, addr,parser)
    elif headers['method'] == "PUT":
        request_PUT(headers, client, addr, parser, msg)
    else:
        not_implemented(headers, client, addr, parser)
        
if __name__ == "__main__":
    host = '127.0.0.1'
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    port = int(sys.argv[1])
    server_socket.bind(('', port))
    server_socket.listen(1)
    #print("Server is ready to listen")


    while True:
        
        try:
            client, addr = server_socket.accept()
            msg = str(datetime.datetime.now()) + " connection has recieved from ip " + str(addr[0]) + " on port " + str(addr[1])
            create_new_log(msg, parser.get('server', 'DebugLog'))
            new_client = threading.Thread(target=response, args=[client, addr, parser])
            # new_client_timeout = threading.Thread(target=timeout, args=[client, addr, parser, ])
            new_client.daemon = True
            # new_client_timeout.daemon = True
            # new_client_timeout.start()
            new_client.start()
            #new_client.join()
        except Exception or OSError as e:
            print(e)
        except KeyboardInterrupt:
            #print("Server has been stopped forcefully")
            sys.exit()