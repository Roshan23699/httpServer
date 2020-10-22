from socket import *
import sys
import os
import datetime
from support_functions import *
from threading import Thread

def request_DEL(dict1, client, addr, ROOT):
    response = "\n"
    # if dict1[1] == "/":
    #     dict1[1] += "index.html"
    content_type = check_extention(dict1[1])
    temp = dict1[1]
    dict1[1] = ROOT
    dict1[1] += temp
    if True: #authoriazation
        if True:
            response += "HTTP/1.1 200 OK\n"
            curr_time = datetime.datetime.now()
            response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
            response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
            content_length = os.path.getsize(dict1[1])
            response += "Content-Length: " + str(content_length) + "\n"
            if content_type == None:
                content_type = "text/html"
            response += "Content-Type: " + content_type + "\n\n"
            response = response.encode()
            response += read_file('../var/www/html/filedeleted.html', content_type)
            response += "\n"
            client.send(response)
            client.close()
        else:
            response += "HTTP/1.1 202 No Content\n"
            response = response.encode()
            client.send(response)
            client.close()
    else:
        dict1[1] = ROOT
        dict1[1] += "/error/error.html"
        curr_time = datetime.datetime.now()
        response += "HTTP/1.1 400 Bad Request\n"
        response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
        response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
        content_length = os.path.getsize(dict1[1])
        response += "Content-Length: " + str(content_length) + "\n"
        response += "Content-Type: text/html; charset=iso-8859-1\n\n"
        response  = response.encode()
        response += read_file(dict1[1], content_type)
        client.send(response)
        if find_value("Connection:", dict1) != "keep-alive":
            client.close()
