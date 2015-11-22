import threading
import time
import socket, subprocess, sys
import thread
import shelve
from datetime import datetime

'''section 1'''
subprocess.call('clear', shell=True)
shelf = shelve.open('mohit.raj')
data = (shelf['desc'])

'''section 2'''
class myThread(threading.Thread):
	def __init(self, rmip, r1, r2, c):
		threading.Thread.__init__(self)
		self.threadName = threadName
		self.rmip = rmip
		self.r1 = r1
		self.r2 = r2
		self.c = c

	def run(self):
		scantcp(self.threadName, self.rmip, self.r1, self.r2, self.c)

'''section 3'''
def scantcp(threadName, rmip, r1, r2, c):
	try:
		for port in range(r1, r2):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(c)
			result = sock.connect_ex((rmip, port))

			if result==0:
				print "Port Open:--->\t", port, "--", data.get(port, "Not in DB")
				sock.close()
		
	except KeyboardInterrupt:
		print "Quit Already"
		sys.exit()

	except socket.gaierror:
		print "Host name cannot be resolved"
		sys.exit()

	except socket.error:
		print "could not connect to server"
		sys.exit()
	
	shelf.close()

'''section 4'''

print "*"*40
print "\t Welcome this is the Port Scanner of Abass"
