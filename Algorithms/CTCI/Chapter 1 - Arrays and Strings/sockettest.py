import socket
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("127.0.0.1",21))
ans = s.recv(1024)
print ans