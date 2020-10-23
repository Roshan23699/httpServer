from socket import *
import sys
import os
import datetime
from support_functions import *
from threading import Thread
from authorization import CHECK_AUTH, authorize
from status_4XX import *
def request_GET(dict1, client, addr, ROOT):
            response = "\n"
            if dict1[1][len(dict1[1]) - 1] == "/":
                   dict1[1] += "index.html"
            #print(dict1[1kjfklal])
            #check the extention of the file to be sent
            content_type = check_extention(dict1[1])
            temp = dict1[1]
            dict1[1] = ROOT
            dict1[1] += temp
            print(dict1)

            if os.path.exists(dict1[1]):
                if(dict1[1] in CHECK_AUTH and not authorize(dict1, client, addr, ROOT)):
                    #return 401 Unauthorized
                    unauthorized(dict1, client, addr, ROOT)
                else :
                    response += "HTTP/1.1 200 OK\n"
                    curr_time = datetime.datetime.now()
                    response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
                    response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
                    last_modified = os.path.getmtime(dict1[1])
                    #response += ("Last-Modified: " + last_modified.strftime("%A") + ", " + last_modified.strftime("%d") +  " " + last_modified.strftime("%b") + " " + last_modified.strftime("%Y") + " " + last_modified.strftime("%X") +  " GMT\n")
                    response += ("last-Modified: " + datetime.datetime.fromtimestamp(last_modified).strftime("%A, %d %b, %Y %I:%M:%S")+ " GMT\n")
                    response += 'ETag: "2aa6-59280a1a3740c"\n'
                    response += "Accept-Ranges: bytes\n"
                    content_length = os.path.getsize(dict1[1])
                    response += "Content-Length: " + str(content_length) + "\n"
                    response += "Vary: Accept-Encoding\n"
                    #content_type = find_value("Content-Type:", dict1)
                    #to avoid any errors for now
                    #fall through
                    if content_type == None:
                        content_type = "text/html"
                    # print(find_value("Connection:", dict1))
                    response += "Content-Type: " + content_type + "\n"
                    if find_value("Connection:", dict1) == "Keep-Alive" or find_value("Connection:", dict1) == "keep-alive":
                        response += "keep-alive: timeout=5, max=100\nConnection: Keep-Alive\n\n"
                    else :
                        response += "\n"
                    response  = response.encode()
                    response += read_file(dict1[1], content_type)
                    client.send(response)
                    if find_value("Connection:", dict1) != "Keep-Alive" and find_value("Connection:", dict1) != "keep-alive":
                        client.close()  
                    
            else :
                dict1[1] = ROOT
                dict1[1] += "/error/notfound.html"
                response += "HTTP/1.1 404 Not Found\n"
                curr_time = datetime.datetime.now()
                response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
                response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
                content_length = os.path.getsize(dict1[1])
                response += "Content-Length: " + str(content_length) + "\n"
                #response += "Connection: close\n"
                response += "Content-Type: text/html; charset=iso-8859-1\n"
                print(find_value("Connection:", dict1))
                if find_value("Connection:", dict1) == "Keep-Alive" or find_value("Connection:", dict1) == "keep-alive":
                    response += "keep-alive: timeout=5, max=100\nConnection: Keep-Alive\n\n"
                else :
                    response += "\n"
                response  = response.encode()
                response += read_file(dict1[1], content_type)
                client.send(response)
                if find_value("Connection:", dict1) != "Keep-Alive" and find_value("Connection:", dict1) != "keep-alive":
                    client.close()  
                #still to check for the max timeout and close the connection remaining

            #fall through
            if False :
                dict1[1] = ROOT
                dict1[1] += "/error/error.html"
                response += "HTTP/1.1 400 Bad Request\n"
                curr_time = datetime.datetime.now()
                response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
                response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
                content_length = os.path.getsize(dict1[1])
                response += "Content-Length: " + str(content_length) + "\n"
                #response += "Connection: close\n"
                response += "Content-Type: text/html; charset=iso-8859-1\n\n"
                response  = response.encode()
                response += read_file(dict1[1], content_type)
                client.send(response)
                if find_value("Connection:", dict1) != "keep-alive":
                    client.close()
