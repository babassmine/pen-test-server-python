import os
import platform
from datetime import datetime
net = raw_input("Enter the Network Address ")
st1 = int(raw_input("Enter Starting Number "))
en1 = int(raw_input("Enter Ending Number "))

oper = platform.system()
if (oper == 'Windows'):
	ping = 'ping -n 1 '
	comp = 'TTL'
else:
	ping = 'ping -c 1 '
	comp = 'ttl'

t1 = datetime.now()
for ip in range(st1, (en1+1)):
	addr = net+'.'+str(ip)
	comm = ping + addr
	response = os.popen(comm)
	for line in response.readlines():
		if (line.count(comp)):
			break
	if (line.count(comp)):
		print addr, "----> LIVE"

t2 = datetime.now()
total = t2 - t1
print "Scanning complete in ", total
