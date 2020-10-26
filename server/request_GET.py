from socket import *
import sys
import os
import datetime
from support_functions import *
from threading import Thread
from authorization import CHECK_AUTH, authorize
from status_4XX import *
<<<<<<< HEAD
def request_GET(headers, client, addr, ROOT):
            response = "\n"
            if headers['request-uri'] == "/":
                   headers['request-uri'] += "index.html"
=======
from request_conditional import *
def request_GET(dict1, client, addr, ROOT):
            response = ""
            if dict1[1][len(dict1[1]) - 1] == "/":
                   dict1[1] += "index.html"
>>>>>>> f677cbc0a855b94f8038fb6c0948511f4c659a9b
            #print(dict1[1kjfklal])
            #check the extention of the file to be sent
            content_type = check_extention(headers['request-uri'])
            temp = headers['request-uri']
            headers['request-uri'] = ROOT
            headers['request-uri'] += temp
            #print(dict1)

            if os.path.exists(headers['request-uri']):
                if(headers['request-uri'] in CHECK_AUTH and not authorize(headers, client, addr, ROOT)):
                    #return 401 Unauthorized
                    unauthorized(headers, client, addr, ROOT)
                else :
                    if conditional_check(dict1):
                        response += "HTTP/1.1 304 Not Modified\n"
                    else :
                        response += "HTTP/1.1 200 OK\n"
                    curr_time = datetime.datetime.now()
                    response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
                    response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
<<<<<<< HEAD
                    last_modified = os.path.getmtime(headers['request-uri'])
=======
                    

                    last_modified = os.path.getmtime(dict1[1])
>>>>>>> f677cbc0a855b94f8038fb6c0948511f4c659a9b
                    #response += ("Last-Modified: " + last_modified.strftime("%A") + ", " + last_modified.strftime("%d") +  " " + last_modified.strftime("%b") + " " + last_modified.strftime("%Y") + " " + last_modified.strftime("%X") +  " GMT\n")
                    response += ("last-Modified: " + datetime.datetime.fromtimestamp(last_modified).strftime("%A, %d %b, %Y %I:%M:%S")+ " GMT\n")
                    response += 'ETag: ' + etag(dict1[1]) + '\n'
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
                not_found(headers, client, addr, ROOT)
                # headers['request-uri']] = ROOT
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
            #     headers['request-uri'] = ROOT
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
