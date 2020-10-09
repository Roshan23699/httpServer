from socket import *
import sys
import os
import datetime

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
    dict1 = msg.split()
    print(dict1)
    #check for the request
    response  = "\n"
    if dict1[0] == "GET":
        if dict1[1] == "/" or dict1[1] == "/index.html":
            dict1[1] = "index.html"
            if os.path.exists(dict1[1]):
                requested_file = open(dict1[1], 'r')
                response += "HTTP/1.1 200 OK\n"
                curr_time = datetime.datetime.now()
                response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
                response += "Server: Apache/2.4.29 (Ubuntu)\n"
                response += "Last-Modified: Sat, 14 Sep 2019 10:14:08 GMT\n"
                response += 'ETag: "2aa6-59280a1a3740c"\n'
                response += "Accept-Ranges: bytes\n"
                response += "Content-Length: 10918\n"
                response += "Vary: Accept-Encoding\n"
                response += "Content-Type: text/html\n\n"

                response += requested_file.read();
                requested_file.close()
                client.send(response.encode())
                client.close()
