from socket import *
import sys
import os
import datetime
from configparser import ConfigParser
from support_functions import *
from log_functions import *
from status_5XX import *
def request_PUT(headers, client, addr, parser, msg):
            response = ""
            content_type = check_extention(headers['request-uri'])
            temp = headers['request-uri']
            headers['request-uri'] = parser.get('server','DocumentRoot')
            headers['request-uri'] += temp

            if os.path.exists(headers['request-uri']):
                if read_file(headers['request-uri'], '') == find_body(msg):
                    response = "HTTP/1.1 204 No Content\n"
                else :
                    if write_file(headers['request-uri'], find_body(msg).encode()):
                        response += "HTTP/1.1 200 OK\n"
                        response += "Content-Location: " + headers['request-uri'] + "\n"
                        curr_time = datetime.datetime.now()
                        response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
                        response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
                        response += "\n"
                        response = response.encode()
                        client.send(response)
                        custom_log(client, addr, curr_time, headers, parser, '200', str(''))
                        if 'Connection' in headers and  headers['Connection'] != "keep-alive":
                            client.close()
                    else :
                        internal_server_error(headers, client, addr, parser)

            else :
                try:
                    write_file(headers['request-uri'], find_body(msg).encode())
                    response += "HTTP/1.1 201 Created\n"
                    response += "Content-Location: " + headers['request-uri'] + "\n"
                    curr_time = datetime.datetime.now()
                    response += ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
                    response += "Server: Aditya-Roshan/1.0.0 (Cn)\n"
                    response += "\n"
                    response = response.encode()
                    client.send(response)
                    custom_log(client, addr, curr_time, headers, parser, '200', str(content_length))
                    if 'Connection' in headers and  headers['Connection'] != "keep-alive":
                        client.close()
                except:
                    internal_server_error(headers, client, addr, parser)
              