import socket

def get_portnumber(prefix):
	return dict( (getattr(socket, a), a)
		for a in dir(socket)
			if a.startswith(prefix))

proto_fam = get_portnumber('AF_')
types = get_portnumber('SOCK_')
protocols = get_portnumber('IPPROTO_')

for res in socket.getaddrinfo('www.thapar.edu', 'http'):
	family, socktype, proto, canonname, sockaddr = res
	
	print 'Family				 :', 	proto_fam[family]
	print 'Type					 :', 	types[socktype]
	print 'Protocol			 :',	protocols[proto]
	print 'Canonical name:',	canonname
	print 'Socket address:',	sockaddr
