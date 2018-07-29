import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('124 234t 34 54y')

data = sock.recv(1024)
sock.close()

print(data)
