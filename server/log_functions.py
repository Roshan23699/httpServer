from socket import *
import sys
import os
import datetime
from configparser import ConfigParser
import logging
from status_5XX import *
def create_new_log(data, file_name):
    f = open(file_name, "a")  # append mode
    f.write("\n")   
    f.write(data)
    f.close()


def error_log(client, addr, curr_time, headers, parser):
    errorlog = "[Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n"
    errorlog += "[error]\n"
    errorlog += "[client " + str(addr[0]) + " ]\n"
    if headers:
        errorlog += "client denied by server configuration:" + headers['request-uri'] + '\n'
    try:
        create_new_log(errorlog, parser.get('server', 'ErrorLog'))
    except:
        internal_server_error(headers, client, addr, parser)

def custom_log(client, addr, curr_time, headers, parser, status_code, content_length):
    customlog = str(addr[0]) + "\n"
    customlog +=  curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n"
    if not 'version' in headers :
        headers['version'] = 'HTTP/1.1'
    customlog +=  headers['method'] + " " + headers['request-uri'] + " " + headers['version'] + "\n"
    customlog +=  status_code + "\n"
    customlog +=  content_length + "\n"
    try:
        create_new_log(customlog, parser.get('server', 'CustomLog'))
    except:
        internal_server_error(headers, client, addr, parser)