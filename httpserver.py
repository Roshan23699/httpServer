
from socket import *
import sys

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
    msg = client.recv(1024).decode('utf-8')
    dict1 = msg.split()
    print(l1)
    break