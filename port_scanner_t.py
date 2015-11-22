import threading
import time
import socket, subprocess, sys
import thread
import shelve
from datetime import datetime

'''section 1'''
subprocess.call('clear', shell=True)
shelf = shelve.open('abass.raj')
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

rmip = ''
d = raw_input("\tPress D for Domain Name or Press for IP Address\t")
if (d=='D' or d=='d'):
	rmserver = raw_input("\tEnter the Domain Name to scann:\t")
	rmip = socket.gethostbyname(rmserver)
elif (d=='I' or d =='I'):
	rmip = raw_input("\tEnter the IP Address to scan: ")

else:
	print "Wrong input"

r11 = int(raw_input("\t Enter the start port number\t"))
r21 = int(raw_input("\t Enter the last port number\t"))

conect = raw_input("For low connectivity press L and High connectivity PressH\t")

if (conect == 'L' or conect == 'l'):
	c = 1.5
elif (conect == 'h' or conect == 'H'):
	c = 0.5

else:
	print "Wrong Input"

print "\Abass' Scanner is working on ", rmip
print "*"*60
t1 = datetime.now()
tp = r21 - r11

tn = 30
tnum = tp/tn

if (tp%tn != 0):
	tnum = tnum + 1

if (tnum > 200):
	tn = tp/300
	tn = tn + 1
	tnum = tp / tn

	if (tp%th !=0 ):
		tnum = tnum + 1

'''section 5'''
threads = []

try:
	for i in range(tnum):
		k=i
		r2=r11+tn
		thread = myThread('T1', rmip, r11,r2, c)
		thread.start()
	threads.append(thread)
	r11 = r2
except:
	print "Error: unable to start thread"


print "\t Number of Threads active:", threading.activeCount()

for t in theads:
	t.join()
print "Exiting Main Thread"
t2 = datetime.now()

total = t2 - t1
print "scanning completed in ", total
