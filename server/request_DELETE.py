from socket import *
import sys
import os
import datetime
from support_functions import *
from threading import Thread
from status_4XX import *
from authorization import *
from status_5XX import *
import re
pending = []
def request_DEL(headers, client, addr, parser):
    global pending
    admin_permission_files = parser.get('server', 'DocumentRoot')
    admin_permission_files += "/volim/"

    response = ""
    # if dict1[1] == "/":
    #     dict1[1] += "index.html"
    content_type = check_extention(headers['request-uri'])
    temp = headers['request-uri']
    headers['request-uri'] = parser.get('server', 'DocumentRoot')
    headers['request-uri'] += temp
    if 'request-uri' in headers:

        f = os.listdir(admin_permission_files)
        if os.path.exists(headers['request-uri']) and os.path.isfile(headers['request-uri']): #authoriazation
            if 'Authorization' in headers and authorize(headers, client, addr, parser) and  not  re.search(admin_permission_files, headers['request-uri']):
                response += "HTTP/1.1 200 OK\n"
                curr_time = datetime.datetime.now()
                response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
                response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
                content_length = os.path.getsize(headers['request-uri'])
                response += "Content-Length: " + str(content_length) + "\n"
                if content_type == None:
                    content_type = "text/html"
                response += "Content-Type: " + content_type + "\n\n"
                response = response.encode()
                response += read_file('../var/www/html/filedeleted.html', content_type)
                try:
                    os.remove(headers['request-uri'])
                    # os.remove("../var/www/html/adminpermission/permission.html")
                    # os.system('sudo rm ' + str(headers['request-uri']))
                except Exception as e:
                    internal_server_error(headers, client, addr, parser)
                    return
                client.send(response)
                client.close()
            elif 'Authorization' in headers and authorize(headers, client, addr, parser) and re.search(admin_permission_files, headers['request-uri']):
                pending.append(headers['request-uri'])
                response += "HTTP/1.1 202 Accepted\n"
                curr_time = datetime.datetime.now()
                response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
                response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
                content_length = os.path.getsize(headers['request-uri'])
                response += "Content-Length: " + str(content_length) + "\n"
                if content_type == None:
                    content_type = "text/html"
                response += "Content-Type: " + content_type + "\n\n"
                # response += "\n"
                response = response.encode()
                #response += read_file('../var/www/html/filedeleted.html', content_type)
                client.send(response)
                client.close()
            else:
                unauthorized(headers, client, addr, parser)
        else:
            not_found(headers, client, addr, parser)