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
    msg = msg.split('\r\n\r\n')
    # print(msg[1])
    return msg[1]



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


def read_file_bytes(f, type_of_file, start, end):
        content = b""
        with open(f, "rb") as f:
            byte = f.read(1)
            while byte != b"":
                # Do stuff with byte.
                content += byte
                byte = f.read(1)
        return content[start:end + 1]

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
        return headers
    except Exception:
        return None


def config_parser():
      
    configur = ConfigParser() 
    configur.read('/etc/Roshan-Aditya/roshanaditya.conf')
    return configur

