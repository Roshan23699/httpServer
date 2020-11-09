from socket import *
import sys
import os
import datetime
from configparser import ConfigParser
import logging



def setCookie(response):
	#just sample cookie is set, doesn't make much sense to hardcoded value but this can be extended
	curr_time = datetime.datetime.now()
	expires = 24 * 60 * 60
	#setting up the expiry time after 1 day, doesn't make sense to hardcode but this can be extended
	curr_time += expires
	#setting up the cookie and its life
	response += "Set-Cookie: user=12123; Expires=" + expires + ";"
	#setting up the secure tag to not allow the man in middle attack
	#the cookie is only sent with the secure (https) http pages inside server can't send the cookie with secure tag
	response += "Secure;"
	#httpOnly will never allow the javascript to extract the cookies 
	#for eg. 'document.cookies' will do nothing
	#also avoids (XSS) attacks
	response += "HttpOnly;"
	#domain tag can also be set which helps browsers to decide to which domains to send the cookie
	#by default for all the subdomains browser sends the cookies
	#response += "Domain = localhost:12000;"

	#all the paths having /post will match 
	#cookie will be sent only if the path is /post/....
	response += "Path=/post;"
	#Samesite has three values
	#Strict will allow the cookies to be sent on the same site
	#Lax : similar to strict but not allow cookies if the site is opened by following a link from external page or domain
	#None: has no restrictions
	response += "SameSite=Strict;"
	#cookie prefixes
	response += "\n"
	return response

def checkCookie(headers):
	#In the actual server lots of operations are to be performed like parsing cookie value as there can be multiple cookies but this server just checks if the cookie is set then just return true else false; this can be extended!
	if('Cookie' in headers and headers['Cookie'] != None):
		cookies = headers['Cookie'].split(';')
		# print("\n\n\n")
		# print(cookies)
		# print("\n\n\n")
		if 'user=12123' in cookies:
			return True
	return False