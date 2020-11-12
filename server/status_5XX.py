from socket import *
import sys
import os
import datetime
from configparser import ConfigParser
from threading import Thread
from support_functions import *
from log_functions import *

def read_file(f, type_of_file):
    #f is the file to be read
    #type_of_file is the extention of file
        content = b""
        with open(f, "rb") as f:
            byte = f.read(1)
            while byte != b"":
                # Do stuff with byte.
                content += byte
                byte = f.read(1)
        return content



def not_implemented(headers, client, addr, parser):
    response = "\n"
    path = parser.get('server', 'DocumentRoot')
    path += "/5XX/not_implemented.html"

    response += "HTTP/1.1 501 Method Not Implemented\n"
    curr_time = datetime.datetime.now()
    response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
    response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
    last_modified = os.path.getmtime(path)
    content_length = os.path.getsize(path)
    response += "Content-Length: " + str(content_length) + "\n"
    #content_type = find_value("Content-Type:", dict1)
    #to avoid any errors for now
    #fall through
    content_type = "text/html"
    response += "Content-Type: " + content_type + "\n\n"
    #response += requested_file.read();
    response = response.encode()
    response += read_file(path, content_type)
    #requested_file.close()#no need of this statement any more
    client.send(response)
    error_log(client, addr, curr_time, headers, parser)
    if 'Connection' in headers and headers['Connection'] != "keep-alive":
        client.close()

def internal_server_error(headers, client, addr, parser):
    response = "\n"
    path = parser.get('server', 'DocumentRoot')
    path += "/5XX/internal_server_error.html"

    response += "HTTP/1.1 500 Internal Server Error\n"
    curr_time = datetime.datetime.now()
    response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
    response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
    last_modified = os.path.getmtime(path)
    content_length = os.path.getsize(path)
    response += "Content-Length: " + str(content_length) + "\n"
    #content_type = find_value("Content-Type:", dict1)
    #to avoid any errors for now
    #fall through
    content_type = "text/html"
    response += "Content-Type: " + content_type + "\n\n"
    #response += requested_file.read();
    response = response.encode()
    response += read_file(path, content_type)
    #requested_file.close()#no need of this statement any more
    client.send(response)
    error_log(client, addr, curr_time, headers, parser)
    if 'Connection' in headers and headers['Connection'] != "keep-alive":
        client.close()


def service_unvailable(headers, client, addr, parser):
    response = "\n"
    path = parser.get('server', 'DocumentRoot')
    path += "/5XX/service_unavailable.html"

    response += "HTTP/1.1 503 Service Unavailable\n"
    curr_time = datetime.datetime.now()
    response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
    response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
    last_modified = os.path.getmtime(path)
    content_length = os.path.getsize(path)
    response += "Content-Length: " + str(content_length) + "\n"
    #content_type = find_value("Content-Type:", dict1)
    #to avoid any errors for now
    #fall through
    content_type = "text/html"
    response += "Content-Type: " + content_type + "\n\n"
    #response += requested_file.read();
    response = response.encode()
    response += read_file(path, content_type)
    #requested_file.close()#no need of this statement any more
    client.send(response)
    error_log(client, addr, curr_time, headers, parser)
    if 'Connection' in headers and  headers['Connection'] != "keep-alive":
        client.close()