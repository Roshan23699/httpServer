from socket import *
import sys
import os
import datetime
from configparser import ConfigParser
from support_functions import *
from log_functions import *
import re

#normally we have to read this from some file at the start of server
CHECK_AUTH = ["/var/www/html/", "/var/www/html/index.html"]


def authorize(headers, client, addr, parser):
	#Here we need to check authorization but just checking if client has send the authorization then
	#assuming that its true
	if 'Authorization' in headers and headers['Authorization'] is not None:
		# print(headers['Authorization'].split()[1])
		print()
		print()
		print()
		print(parser.get('credentials', 'users'))
		if parser.get('credentials', 'users') in  headers['Authorization'].split():
			return True
		return False
	# print("hello")
	return False