from socket import *
import sys
import os
import datetime
import mimetypes
import re
import email
from configparser import ConfigParser
from io import StringIO
import status_5XX 
#function to find the msg body of the request or even response if needed
def find_body(msg):
    msg.split('\n\n')
    return msg[1]
#function to check headers and finding their values
# def find_value(x, y):
#     #x is the attribute of which value is to be found
#     #y is the array in which the value to be found
#     t = False
#     for val in y:
#         if t :
#             return val
#         if val == x:
#             t = True
#     return None


#function to return the extention of the file
def check_extention(x):
    return mimetypes.guess_type(x)[0]


#type of file doesn't make any sense as we are reading a binary file
def read_file(f, type_of_file):
    #f is the file to be read
    #type_of_file is the extention of file
    if os.path.isfile(f):
        content = b""
        with open(f, "rb") as f:
            byte = f.read(1)
            while byte != b"":
                # Do stuff with byte.
                content += byte
                byte = f.read(1)
        return content

def write_file(f, content):
    #f is the file to be written
    #here the content is assumed to be binary
    try:
        with open(f, "wb") as f:
            f.write(content)
        return True
    except:
        return False


def check_header(msg):
    
    try:
        # pop the first line so we only process headers
        _, headers = msg.split('\r\n', 1)

        # construct a message from the request string
        message = email.message_from_file(StringIO(headers))

        # construct a dictionary containing the headers
        headers = dict(message.items())
        # print("\n\n\n\n")
        # print(headers)
        # print("\n\n\n\n")
        # # pretty-print the dictionary of headers
        # pprint.pprint(headers, width=160)
        return headers
    except Exception:
        return None


def config_parser():
      
    configur = ConfigParser() 
    configur.read('/etc/Roshan-Aditya/roshanaditya.conf')
    return configur

def check_credential(headers):
    auth = headers['Authorization'].split()[1]
    print(auth)
    try:
        if str(auth.decode()) in open('../etc/Roshan-Aditya/auth.conf').read() :
            return True
        else:
            False
    except:
        return True