from socket import *
import sys
import os
import datetime
from support_functions import *

def check_etag(et, resource) :
	if etag is not None and et == etag(resource):
		return True
	else :
		return False


def conditional_check(headers):
	#for now just checking based on etag
	resource = headers['request-uri']
	if 'Etag' in headers:
		etag = headers['Etag']
	if check_etag(etag, resource):
		return True
	else :
		return False
