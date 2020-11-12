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
from status_3XX import moved_permanentely
def request_GET(headers, client, addr, parser):
    # response = "\n"
    response = ""
    if headers['request-uri'][len(headers['request-uri']) - 1] == "/":
        headers['request-uri'] += "index.html"
    if(headers['request-uri'] in MOVED_PERMANENTELY):
        moved_permanentely(headers, client, addr, parser)
    #check the extention of the file to be sent
    content_type = check_extention(headers['request-uri'])
    temp = headers['request-uri']
    headers['request-uri'] = parser.get('server', 'DocumentRoot')
    headers['request-uri'] += temp

    if os.path.exists(headers['request-uri']):
        if(headers['request-uri'] in CHECK_AUTH and not authorize(headers, client, addr, parser)):
            #return 401 Unauthorized
            unauthorized(headers, client, addr, parser)
        else :
            if conditional_if_range(headers):
                # response += "HTTP/1.1 206 Partial Content\n"
                partial_content(headers, client, addr, parser)
                return
            elif conditional_check(headers):
            # if False:
                response += "HTTP/1.1 304 Not Modified\n"
            else :
                response += "HTTP/1.1 200 OK\n"
            if checkCookie(headers):
                #don't send cookie for now
                # print("\n\n\n\n")
                # print(headers)
                # print("\n\n\n\n")
                pass
            else :
                response = setCookie(response)
            curr_time = datetime.datetime.now()
            response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
            response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
            last_modified = os.path.getmtime(headers['request-uri'])
            response += ("last-Modified: " + datetime.datetime.fromtimestamp(last_modified).strftime("%A, %d %b, %Y %I:%M:%S")+ " GMT\n")
            if not 'If-None-Match' in headers:
                response += 'ETag: ' + etag(headers['request-uri']) + '\n'
                response = setCasheControl(response, maxAge=10)
            response += "Accept-Ranges: bytes\n"
            content_length = os.path.getsize(headers['request-uri'])
            response += "Content-Length: " + str(content_length) + "\n"
            response += "Vary: Accept-Encoding\n"
            if content_type == None:
                content_type = "text/html"
            if 'Accept' in headers:
                if not ('*/*' in headers['Accept']  or content_type in headers['Accept']):
                    bad_request(headers,client, addr, parser)
            response += "Content-Type: " + content_type + "\n"
            if 'Connection' in headers and headers['Connection'] != "keep-alive":
                response += "keep-alive: timeout=5, max=100\nConnection: Keep-Alive\n\n"
            else :
                response += "\n"
            response  = response.encode()
            response += read_file(headers['request-uri'], content_type)
            client.send(response)
            custom_log(client, addr, curr_time, headers, parser, '200', str(content_length))
            if 'Connection' in headers and headers['Connection'] != "keep-alive":
                    client.close()  
                    
    else :
        not_found(headers, client, addr, parser)
              
          