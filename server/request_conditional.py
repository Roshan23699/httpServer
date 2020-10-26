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


def conditional_check(dict1):
	#for now just checking based on etag
	resource = dict1[1]
	etag = find_value("ETag:", dict1)
	if check_etag(etag, resource):
		return True
	else :
		return False
