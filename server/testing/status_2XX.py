from socket import *
import sys
import os
import datetime
from support_functions import *
from threading import Thread
from log_functions import *





def conditional_if_range(headers):
    path = parser.get('server','DocumentRoot')
    path += headers['request-uri']
    response = ""
    response += "HTTP/1.1 206 Partial Content\n"
    curr_time = datetime.datetime.now()
    response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
    response += ("Location: " + MOVED_PERMANENTELY[headers['request-uri']]) + "\n"
    response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"

    bytes_range = headers['Range'].split("=")[1].split('-')
    content_length = bytes_ranges[1] - bytes_ranges[0] + 1
    response += "Content-Length: " + str(content_length) + "\n"
    content_length = os.path.getsize(path)
    response += "Content-Type: " + content_type + "\n\n"
    response += "\n"
    response = response.encode()
    response += read_file_bytes(path, 'text/html', bytes_range[0], bytes_range[1])
    client.send(response)
    access_log(client, addr, curr_time, headers, parser)
    client.close()
