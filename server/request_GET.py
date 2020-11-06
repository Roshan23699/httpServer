from socket import *
import sys
import os
import datetime
from support_functions import *
from threading import Thread
from request_conditional import *
from authorization import CHECK_AUTH, authorize
from status_4XX import *
def request_GET(headers, client, addr, parser):
    response = "\n"
    if headers['request-uri'] == "/":
        headers['request-uri'] += "index.html"
            #print(dict1[1kjfklal])
            #check the extention of the file to be sent
    content_type = check_extention(headers['request-uri'])
    temp = headers['request-uri']
    headers['request-uri'] = parser.get('server', 'DocumentRoot')
    headers['request-uri'] += temp
            #print(dict1)

    if os.path.exists(headers['request-uri']):
        if(headers['request-uri'] in CHECK_AUTH and not authorize(headers, client, addr, parser)):
            #return 401 Unauthorized
            unauthorized(headers, client, addr, parser)
        else :
            # if conditional_check(headers):
            if True:
                response += "HTTP/1.1 304 Not Modified\n"
            else :
                response += "HTTP/1.1 200 OK\n"
                curr_time = datetime.datetime.now()
                response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
                response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
                last_modified = os.path.getmtime(headers['request-uri'])
                #response += ("Last-Modified: " + last_modified.strftime("%A") + ", " + last_modified.strftime("%d") +  " " + last_modified.strftime("%b") + " " + last_modified.strftime("%Y") + " " + last_modified.strftime("%X") +  " GMT\n")
                response += ("last-Modified: " + datetime.datetime.fromtimestamp(last_modified).strftime("%A, %d %b, %Y %I:%M:%S")+ " GMT\n")
                if 'Etag' in headers:
                    response += 'ETag: ' + headers['Etag']+ '\n'
                response += "Accept-Ranges: bytes\n"
                content_length = os.path.getsize(headers['request-uri'])
                response += "Content-Length: " + str(content_length) + "\n"
                response += "Vary: Accept-Encoding\n"
                #content_type = find_value("Content-Type:", dict1)
                #to avoid any errors for now
                #fall through
                if content_type == None:
                    content_type = "text/html"
                # print(find_value("Connection:", dict1))
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
                if 'Connection' in headers and headers['Connection'] != "keep-alive":
                        client.close()  
                    
    else :
        not_found(headers, client, addr, parser)
                # headers['request-uri']] = parser
                # headers['request-uri']] += "/error/notfound.html"
                # response += "HTTP/1.1 404 Not Found\n"
                # curr_time = datetime.datetime.now()
                # response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
                # response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
                # content_length = os.path.getsize(headers['request-uri']])
                # response += "Content-Length: " + str(content_length) + "\n"
                # #response += "Connection: close\n"
                # response += "Content-Type: text/html; charset=iso-8859-1\n"
                # print(find_value("Connection:", dict1))
                # if headers['Connection'] != "keep-alive":
                #         response += "keep-alive: timeout=5, max=100\nConnection: Keep-Alive\n\n"
                # else :
                #         response += "\n"
                # response  = response.encode()
                # response += read_file(headers['request-uri'], content_type)
                # client.send(response)
                # if headers['Connection'] != "keep-alive":
                #         client.close() 
                #still to check for the max timeout and close the connection remaining

            #fall through
            # if False :
            #     headers['request-uri'] = parser
            #     headers['request-uri']] += "/error/error.html"
            #     response += "HTTP/1.1 400 Bad Request\n"
            #     curr_time = datetime.datetime.now()
            #     response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
            #     response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
            #     content_length = os.path.getsize(headers['request-uri']])
            #     response += "Content-Length: " + str(content_length) + "\n"
            #     #response += "Connection: close\n"
            #     response += "Content-Type: text/html; charset=iso-8859-1\n\n"
            #     response  = response.encode()
            #     response += read_file(headers['request-uri']], content_type)
            #     client.send(response)
            #     if headers['Connection'] != "keep-alive":
            #             client.close()
