import socket

host = "10.0.0.167"

port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
data, addr = s.recvfrom(1024)
print "recieved from ",addr
print "obtained ",data

s.close()
