from socket import *
import sys
import os
import datetime
from configparser import ConfigParser
from support_functions import *
from log_functions import *
from authorization import CHECK_AUTH

def unauthorized(headers, client, addr, parser):
    path = parser.get('server','DocumentRoot')
    path += "/error/error.html"
    verification_details = parser.get('server','DocumentRoot') + "/post/form.html"
    response = "\n"
    response += "HTTP/1.1 401 Unauthorized\n"
    curr_time = datetime.datetime.now()
    response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
    response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
    response += ("WWW-Authenticate: Basic realm=" + verification_details + "\n")
    if headers['Connection'] != "keep-alive":
        response += "keep-alive: timeout=5, max=100\nConnection: Keep-Alive\n\n"
    else :
        response += "\n"
    response  = response.encode()
    content_type = "text/html"
    response += read_file(path, 'text/html')
    client.send(response)
    error_log(client, addr, curr_time, headers, parser)
    if 'Connection' in headers and headers['Connection'] != "keep-alive":
        client.close() 

def bad_request(headers, client, addr, parser):
    path = parser.get('server','DocumentRoot')
    path += "/error/error.html"
    response = "\n"
    response += "HTTP/1.1 404 Bad Request\n"
    curr_time = datetime.datetime.now()
    response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
    response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
    content_length = os.path.getsize(path)
    response += "Content-Length: " + str(content_length) + "\n"
    response += "Connection: close" + "\n"
    response += "Content-Type: " + content_type + "\n\n"
    response = response.encode()
    response += read_file(path, 'text/html')
    client.send(response)
    error_log(client, addr, curr_time, headers, parser)
    client.close()

def not_found(headers, client, addr, parser):
    path = parser.get('server','DocumentRoot')
    path += "/error/notfound.html"
    response = "\n"
    response += "HTTP/1.1 404 Not Found\n"
    curr_time = datetime.datetime.now()
    response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
    response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
    content_length = os.path.getsize(path)
    response += "Content-Length: " + str(content_length) + "\n"
    #response += "Connection: close\n"
    response += "Content-Type: text/html; charset=iso-8859-1\n"
    #print(find_value("Connection:", dict1))
    if headers['Connection'] != "keep-alive":
        response += "keep-alive: timeout=5, max=100\nConnection: Keep-Alive\n\n"
    else :
        response += "\n"
    response  = response.encode()
    response += read_file(path, 'text/html')
    client.send(response)
    error_log(client, addr, curr_time, headers, parser)
    if 'Connection' in headers and  headers['Connection'] != "keep-alive":
        client.close() 