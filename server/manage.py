import os, signal, sys, threading

def start(arg):
	if(arg == "start"):
		os.system("sudo python3 httpserver.py 12000 > temp.txt &")
	else :
		for line in os.popen("ps -eaf | grep 12000 | grep -v grep"):  
				fields = line.split() 
				# print(line[0])
				# print(fields[1])
				os.system('kill -9 ' + str(fields[1]))
if __name__ == "__main__":
	server_thread = threading.Thread(target=start, args=[sys.argv[1]])
	server_thread.start()