import socket

c = socket.socket()
print('socket Created.')

c.connect(('192.168.68.104', 9999))

name = input("Enter Your Name:")
c.send(bytes(name, 'utf-8'))

print("connecting...")
print(c.recv(1024).decode())