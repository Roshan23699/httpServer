from socket import *
import sys
import os
import datetime
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
    #if x == html return text/html
    t = x.split(".")
    if t[1] == "html" or t[1] == "htm" :
        return "text/html"
    elif t[1] == "png" or t[1] == "jpg" or t[1] == "jpeg" or t[1] == "gif":
        return "image/" + t[1]
    else :
        return "text/html"

def read_file(f, type_of_file):
    #f is the file to be read
    #type_of_file is the extention of file
    type_of_file = type_of_file.split("/")[0]
    if type_of_file == "text":
        requested_file = open(f,  'r')
        content = requested_file.read()
        requested_file.close()
        return  content.encode()
    elif type_of_file == "image":
        content = b""
        with open(f, "rb") as f:
            byte = f.read(1)
            while byte != b"":
                # Do stuff with byte.
                content += byte
                byte = f.read(1)
        return content
    else :
        raise argparse.ArgumentTypeError(
                'Not a text file! Argument filename must be of type *.txt')

