from socket import *
import sys
import os
import datetime
from configparser import ConfigParser
from support_functions import *
from log_functions import *

#normally we have to read this from some file at the start of server
CHECK_AUTH = ["../var/www/html/", "../var/www/html/index.html"]


def authorize(headers, client, addr, parser):
	#Here we need to check authorization but just checking if client has send the authorization then
	#assuming that its true
	
	if 'Authorization' in headers and headers['Authorization'] is not None:
		credentials = headers['Authorization']
		credentials = credentials.split('&')
		for _ in credentials:
			_ = _.split('=')
		username = None
		password = None
		if credentials[0][0] == 'username':
			username = credentials[0][1]
			password = credentials[1][1]
		elif credentials[1][0] == 'username':
			username = credentials[1][1]
			password = credentials[0][1]

		if username is not None and parser.get('credentials', username):
			return True
	return False