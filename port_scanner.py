import socket, subprocess, sys
from datetime import datetime

subprocess.call('clear', shell=True)
rmip = raw_input ("\tEnter Remote host IP to scan:")
r1 = int(raw_input("\tEnter the start port number\t"))
r2 = int (raw_input("\tEnter the last port number\t"))
r2 = r2 + 1
print "*"*40
print "Abass' Scanner is wokring on ", rmip
print "*"*40
t1 = datetime.now()
try:
	for port in xrange(r1, r2):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)

		result = sock.connect_ex((rmip, port))
		if result==0:
			print "Port Open:--->\t", port
		sock.close()

except KeyboardInterrupt:
	print "Quit Already?"
	sys.exit()

except socket.gaierror:
	print "Host name could not be resolved"
	sys.exit()

except socket.error:
	print "could not connect to server"
	sys.exit()

t2 = datetime.now()

total = t2 - t1
print 'Scanning complete in ', total
