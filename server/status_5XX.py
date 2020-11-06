from socket import *
import sys
import os
import datetime
from configparser import ConfigParser
from support_functions import *
from threading import Thread
def not_implemented(headers, client, addr, parserT):
    response = "\n"
    headers['request-uri'] = parser.get('server', 'DocumentRoot')
    headers['request-uri'] += "/5XX/not_implemented.html"

    response += "HTTP/1.1 501 Method Not Implemented\n"
    curr_time = datetime.datetime.now()
    response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
    response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
    last_modified = os.path.getmtime(headers['request-uri'])
    content_length = os.path.getsize(headers['request-uri'])
    response += "Content-Length: " + str(content_length) + "\n"
    #content_type = find_value("Content-Type:", dict1)
    #to avoid any errors for now
    #fall through
    content_type = "text/html"
    response += "Content-Type: " + content_type + "\n\n"
    #response += requested_file.read();
    response = response.encode()
    response += read_file(headers['request-uri'], content_type)
    #requested_file.close()#no need of this statement any more
    client.send(response)
    error_log(client, addr, curr_time, headers, parser)
    if 'Connection' in headers and headers['Connection'] != "keep-alive":
        client.close()

def internal_server_error(dict1, client, addr, parser):
    response = "\n"
    headers['request-uri'] = parser.get('server', 'DocumentRoot')
    headers['request-uri'] += "/5XX/internal_server_error.html"

    response += "HTTP/1.1 500 Internal Server Error\n"
    curr_time = datetime.datetime.now()
    response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
    response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
    last_modified = os.path.getmtime(headers['request-uri'])
    content_length = os.path.getsize(headers['request-uri'])
    response += "Content-Length: " + str(content_length) + "\n"
    #content_type = find_value("Content-Type:", dict1)
    #to avoid any errors for now
    #fall through
    content_type = "text/html"
    response += "Content-Type: " + content_type + "\n\n"
    #response += requested_file.read();
    response = response.encode()
    response += read_file(headers['request-uri'], content_type)
    #requested_file.close()#no need of this statement any more
    client.send(response)
    error_log(client, addr, curr_time, headers, parser)
    if 'Connection' in headers and headers['Connection'] != "keep-alive":
        client.close()


def service_unvailable(dict1, client, addr, parser):
    response = "\n"
    headers['request-uri'] = parser.get('server', 'DocumentRoot')
    headers['request-uri'] += "/5XX/service_unavailable.html"

    response += "HTTP/1.1 503 Service Unavailable\n"
    curr_time = datetime.datetime.now()
    response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
    response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
    last_modified = os.path.getmtime(headers['request-uri'])
    content_length = os.path.getsize(headers['request-uri'])
    response += "Content-Length: " + str(content_length) + "\n"
    #content_type = find_value("Content-Type:", dict1)
    #to avoid any errors for now
    #fall through
    content_type = "text/html"
    response += "Content-Type: " + content_type + "\n\n"
    #response += requested_file.read();
    response = response.encode()
    response += read_file(headers['request-uri'], content_type)
    #requested_file.close()#no need of this statement any more
    client.send(response)
    error_log(client, addr, curr_time, headers, parser)
    if 'Connection' in headers and  headers['Connection'] != "keep-alive":
        client.close()