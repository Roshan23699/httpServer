from socket import *
import sys
import os
import datetime
from support_functions import *
from threading import Thread
def not_implemented(dict1, client, addr, ROOT):
            response = "\n"
            dict1[1] = ROOT
            dict1[1] += "/5XX/not_implemented.html"

            response += "HTTP/1.1 501 Method Not Implemented\n"
            curr_time = datetime.datetime.now()
            response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
            response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
            last_modified = os.path.getmtime(dict1[1])
            content_length = os.path.getsize(dict1[1])
            response += "Content-Length: " + str(content_length) + "\n"
            #content_type = find_value("Content-Type:", dict1)
            #to avoid any errors for now
            #fall through
            content_type = "text/html"
            response += "Content-Type: " + content_type + "\n\n"
            #response += requested_file.read();
            response = response.encode()
            response += read_file(dict1[1], content_type)
            #requested_file.close()#no need of this statement any more
            client.send(response)
            if find_value("Connection:", dict1) != "keep-alive":
                client.close()
