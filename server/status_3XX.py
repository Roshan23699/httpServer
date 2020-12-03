from socket import *
import sys
import os
import datetime
from support_functions import *
from threading import Thread
from request_conditional import *
from log_functions import *
from authorization import CHECK_AUTH, authorize
from status_4XX import *
from cookies import setCookie, checkCookie
from Moved_Permanentely import MOVED_PERMANENTELY


def moved_permanentely(headers, client, addr, parser):
    path = parser.get('server','DocumentRoot')
    path += "/error/movedpermanentely.html"
    response = "\n"
    response += "HTTP/1.1 301 Moved Permanentely\n"
    curr_time = datetime.datetime.now()
    response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
    response += ("Location: " + MOVED_PERMANENTELY[headers['request-uri']]) + "\n"
    response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
    content_length = os.path.getsize(path)
    response += "Content-Length: " + str(content_length) + "\n"
    # response += "Connection: close" + "\n"
    # response += "Content-Type: " + content_type + "\n\n"
    response += "\n"
    response = response.encode()
    response += read_file(path, 'text/html')
    client.send(response)
    error_log(client, addr, curr_time, headers, parser)
    client.close()
