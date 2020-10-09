from socket import *
import sys
import os
import datetime

#Global Section
ROOT = "../var/www/html/"

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
            dict1[1] = ROOT
            dict1[1] += "index.html"

            if os.path.exists(dict1[1]):
                requested_file = open(dict1[1], 'r')
                response += "HTTP/1.1 200 OK\n"
                curr_time = datetime.datetime.now()
                response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
                response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
                last_modified = os.path.getmtime(dict1[1])
                #response += ("Last-Modified: " + last_modified.strftime("%A") + ", " + last_modified.strftime("%d") +  " " + last_modified.strftime("%b") + " " + last_modified.strftime("%Y") + " " + last_modified.strftime("%X") +  " GMT\n")
                response += ("last-Modified: " + datetime.datetime.fromtimestamp(last_modified).strftime("%A, %d %b, %Y %I:%M:%S")+ " GMT\n")
                response += 'ETag: "2aa6-59280a1a3740c"\n'
                response += "Accept-Ranges: bytes\n"
                response += "Content-Length: 10918\n"
                response += "Vary: Accept-Encoding\n"
                response += "Content-Type: text/html\n\n"

                response += requested_file.read();
                requested_file.close()
                client.send(response.encode())
                client.close()
            else :
                response += "HTTP/1.1 400 Bad Request\n"
                curr_time = datetime.datetime.now()
                response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
                response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
                response += "Content-Length: 330\n"
                response += "Connection: close\n"
                response += "Content-Type: text/html; charset=iso-8859-1\n\n"
                dict1[1] = ROOT
                dict1[1] += "error/error.html"
                requested_file = open(dict1[1], 'r')
                response += requested_file.read();
                requested_file.close()
                client.send(response.encode())
                client.close()


