from socket import *
import sys
import os
import datetime
import mimetypes
import re
import email
from io import StringIO
import status_5XX 
#function to find the msg body of the request or even response if needed
def find_body(msg):
    msg.split('\n\n')
    return msg[1]
#function to check headers and finding their values
def find_value(x, y):
    #x is the attribute of which value is to be found
    #y is the array in which the value to be found
    t = False
    for val in y:
        if t :
            return val
        if val == x:
            t = True
    return None


#function to return the extention of the file
def check_extention(x):
    return mimetypes.guess_type(x)[0]

def read_file(f, type_of_file):
    #f is the file to be read
    #type_of_file is the extention of file
        content = b""
        with open(f, "rb") as f:
            byte = f.read(1)
            while byte != b"":
                # Do stuff with byte.
                content += byte
                byte = f.read(1)
        return content


# def check_header(msg):
#     l = []
#     for i in msg.split('\r\n'):
#         if "GET" in i or "POST" in i or "DELETE" in i or "POST" in i:
#             l.append(split_header_line(i))
#         if "host" in i.lower():
#             l.append(split_header_line(i))
#         if "accept-charset" in i.lower():
#             l.append(split_header_line(i))
#         if "accept-encoding" in i.lower():
#             l.append(split_header_line(i))
#         if "accept-language" in i.lower():
#             l.append(split_header_line(i))
#         if "accept" in i.lower():
#             l.append(split_header_line(i))
#         if "authorization" in i.lower():
#             l.append(split_header_line(i))
#         if "expect" in i.lower():
#             l.append(split_header_line(i))
#         if "from" in i.lower():
#             l.append(split_header_line(i))
#         if "if-match" in i.lower():
#             l.append(split_header_line(i))
#         if "if-modified-since" in i.lower():
#             l.append(split_header_line(i))
#         if "if-none-match" in i.lower():
#             l.append(split_header_line(i))
#         if "if-range" in i.lower():
#             l.append(split_header_line(i))
#         if "if-unmodified-since" in i.lower():
#             l.append(split_header_line(i))
#         if "max-forwards" in i.lower():
#             l.append(split_header_line(i))
#         if "proxy-authorization" in i.lower():
#             l.append(split_header_line(i))
#         if "range" in i.lower():
#             l.append(split_header_line(i))
#         if "referer" in i.lower():
#             l.append(split_header_line(i))
#         if "user-agent" in i.lower():
#             l.append(split_header_line(i))
#         # else:
#         #     return None
#     return l

# def split_header_line(line):
#     return line.split(' ')

def check_header(msg):
    
    try:
        # pop the first line so we only process headers
        _, headers = msg.split('\r\n', 1)

        # construct a message from the request string
        message = email.message_from_file(StringIO(headers))

        # construct a dictionary containing the headers
        headers = dict(message.items())

        # print(headers)
        # # pretty-print the dictionary of headers
        # pprint.pprint(headers, width=160)
        return headers
    except Exception:
        return None