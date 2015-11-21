import threading
import time
import socket, subprocess, sys
import thread
import collections
from datetime import datetime

'''section 1'''
net = raw_input("Enter Network Address ")
st1 = int(raw_input("Enter starting number "))
en1 = int(raw_input("Enter last number "))
en1 = en1 + 1

dic = collections.OrderedDict()

t1 = datetime.now()
'''section 2'''
class myThread(threading.Thread):
	def __init__(self, st, en):
		threading.Thread.__init__(self)
		self.st = st
		self.en = en

	def run(self):
		run1(self.st, self.en)

'''section 3'''
def scan(addr):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	result = sock.connect_ex((addr, 80))
	if result==0:
		sock.close()
		return 1
	else:
		sock.close()

def run1(st1, en1):
	for ip in xrange(st1, en1):
		addr = net + '.' + str(ip)
		if scan(addr):
			dic[ip] = addr

'''section 4'''
total_ip = en1 - st1
tn = 20
total_thread = total_ip / tn
total_thread = total_thread + 1
threads = []

try:
	for i in xrange(total_thread):
		en = st1 + tn
		if (en > en1):
			en = en1
		thread = myThread(st1, en)
		thread.start()
		threads.append(thread)
		st1 = en
except:
	print "Error: unable to start thread "

print "\t Number of Threads active:", threading.activeCount()
for t in threads:
	t.join()
print "Exiting Main Thread"

dict = collections.OrderedDict(sorted(dic.items()))

for key in dict:
	print dict[key], "----> Live"

t2 = datetime.now()
total = t2 - t1
print "scanning complete in ", total
