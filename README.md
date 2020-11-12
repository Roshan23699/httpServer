# httpServer
Http server(Computer Networks Project)

This project is implementation of http server. As part of academic curriculum project , we are implementing  httpServer.


How to start, stop and restart the server:
	goto server/ directory and execute
	python3 manage.py start to start
	python3 manage.py restart to restart
	python3 manage.py stop to stop the server

How to run tests:
	goto server/ directory and execute
	python3 test_get.py
	python3 test_head.py
	python3 test_put.py
	python3 test_post.py
	python3 test_delete.py

for get request  authorization,  the username and password is abc and abc respectively.

to create a request with authorization header add  'Authorization: Basic YWJjOmFiYw==' header for put and delete request
otherwise server sends 401 Unauthorized

web pages should be added at local /var/www/html/ directory
log files should be added at local /var/log/Roshan-Aditya/ directory
config file should be added at /etc/Roshan-Aditya/ directory



