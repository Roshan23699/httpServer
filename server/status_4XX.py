from socket import *
import sys
import os
import datetime
from support_functions import *
from log_functions import *
from authorization import CHECK_AUTH

def unauthorized(dict1, client, addr, ROOT):
    dict1[1] = ROOT
    dict1[1] += "/error/error.html"
    verification_details = ROOT + "/post/form.html"
    response = "\n"
    response += "HTTP/1.1 401 Unauthorized\n"
    curr_time = datetime.datetime.now()
    response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
    response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
    response += ("WWW-Authenticate: Basic realm=" + verification_details + "\n")
    if find_value("Connection:", dict1) == "Keep-Alive" or find_value("Connection:", dict1) == "keep-alive":
        response += "keep-alive: timeout=5, max=100\nConnection: Keep-Alive\n\n"
    else :
        response += "\n"
    response  = response.encode()
    content_type = "text/html"
    response += read_file(dict1[1], content_type)
    client.send(response)
    if find_value("Connection:", dict1) != "Keep-Alive" and find_value("Connection:", dict1) != "keep-alive":
        client.close()
