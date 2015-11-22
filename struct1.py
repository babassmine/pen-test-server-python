import struct 
import socket

host = '10.0.0.146'
port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(1)
conn, addr = sock.accept()
print 'Connected by', addr
msz = struct.pack('hh1', 1,2,3)
conn.send(msz)
conn.close()
