import socket

host = "10.0.0.167" # server address
port =  12345 # port of server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket
s.bind((host,port)) #bind server - connects address to socket
s.listen(2) # starts the tcp listener
conn, addr = s.accept() # use to accept connection from client
print addr, "Now connected"
conn.send("Thank you for connecting") # send data to the socket
conn.close()


