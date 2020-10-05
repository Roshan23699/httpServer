
from socket import *
import sys

host = '127.0.0.1'
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
port = int(sys.argv[1])
server_socket.bind((host, port))
server_socket.listen(1)
print("Server is ready to listen")
