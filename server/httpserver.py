from socket import *
import sys
import os
import datetime
from request_GET import request_GET
from support_functions import *
from request_HEAD import request_HEAD

#Global Section
ROOT = "../var/www/html"




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
        msg = client.recv(1024).decode('utf-8')
        #while not (msg[len(msg) - 2] == '\n' and msg[len(msg) - 1] == '\n'):
            #msg += client.recv(1024).decode('utf-8')
            #print(msg)
        dict1 = msg.split()
        if len(dict1) == 0:
            continue
        print(dict1)
        #check for the request
        if dict1[0] == "GET":
            request_GET(dict1, client, addr, ROOT)
        elif dict1[0] == "HEAD":
            request_HEAD(dict1, client, addr, ROOT)
