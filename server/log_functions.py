from socket import *
import sys
import os
import datetime



def create_new_log(data, file_name):
    f = open(file_name, "a")  # append mode
    f.write("\n")
    f.write(data)
    f.close()



