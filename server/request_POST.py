from socket import *
import sys
import os
import datetime
from support_functions import *

def request_POST(dict1, client, addr, ROOT):
    response = "\n"
    if dict1[1] == "/":
        dict1[1] += "index.html"
    #print(dict1[1kjfklal])
    #check the extention of the file to be sent
    content_type = check_extention(dict1[1])
    temp = dict1[1]
    dict1[1] = ROOT
    dict1[1] += temp
    print(dict1)