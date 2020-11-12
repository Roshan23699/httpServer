from socket import *
import sys
import os
import datetime
from support_functions import *
import hashlib 

def conditional_if_range(headers):
	if(conditional_check(headers)):
		#considering the unit is bytes
		if 'Range' in headers:
			return True
		else :
			return False
	else :
		return False	

def setCasheControl(response, maxAge):
	response += "Cache-Control: max-age=" + str(maxAge) + "\n"
	return response

def etag(resource):
	#for etag md5 hash is used
	return (hashlib.md5(resource.encode())).hexdigest()

def check_etag(et, resource) :
	if et is not None and et == etag(resource):
		return True
	else :
		return False


def conditional_check(headers):
	#for now just checking based on etag
	resource = headers['request-uri']
	if 'If-None-Match' in headers:
		et = headers['If-None-Match']
		if check_etag(et, resource):
			return True
	return False
