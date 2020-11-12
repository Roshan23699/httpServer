import os, signal, sys
if __name__ == "__main__":
	if(sys.argv[1] == "start"):
		os.system("sudo python3 httpserver.py 12000 &")
	elif (sys.argv[1] == 'restart'):
		for line in os.popen("ps -eaf | grep 12000 | grep -v grep"):  
				fields = line.split() 
				# print(line[0])
				# print(fields[1])
				os.system('kill -9 ' + str(fields[1]))
				break
		os.system("sudo python3 httpserver.py 12000 &")
	else :
		for line in os.popen("ps -eaf | grep 12000 | grep -v grep"):  
				fields = line.split() 
				# print(line[0])
				# print(fields[1])
				os.system('kill -9 ' + str(fields[1]))