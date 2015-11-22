import shelve

def create():
	shelf = shelve.open('abass.raj', writeback=True)
	shelf['desc'] = {}
	shelf.close()
	print 'Dictionary was created'

def update():
	shelf = shelve.open('abass.raj', writeback=True)
	data = (shelf['desc'])
	port = int (raw_input('Enter the Port: '))
	data[port] = raw_input("\nEnter the description\t")
	shelf.close()

def del1():
	shelf = shelve.open('abass.raj', writeback=True)
	data = (shelf['desc'])
	port = int(raw_input("Enter the Port: "))
	del data[port]
	shelf.close()
	print "\nEntry is deleted"

def list1():
	print "*"*30
	shelf = shelve.open('abass.raj', writeback=True)
	data = (shelf['desc'])
	for key, value in data.items():
		print key, ':', value
		print '*'*30

print "\tProgram to Update or Add and Delete the port number detail\n"
while(1):
	print "Press"
	print "C for create inly one time create"
	print "U for update or Add\nD for Delete\nL for List all values"
	print "E for exit "
	c = raw_input("Enter : ")

if (c=='C' or c=='c'):
	create()
elif (c=='U' or c=='u'):
	update()
elif(c=='D' or c=='d'):
	del1()
elif(c=='L' or c=='l'):
	list1()
elif(c=='E' or c=='e'):
	exit()
else:
	print "\tWrong Input"


