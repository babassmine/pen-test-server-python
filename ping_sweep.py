import os
import platform
net = raw_input("Enter the Network Address ")
st1 = int(raw_input("Enter Starting Number "))
en1 = int(raw_input("Enter Ending Number "))

oper = platform.system()
if (oper == 'Windows'):
	ping = 'ping -n 1'
else:
	ping = 'ping -c 1'

for i in range(st1, en1):
	

