import socket


s = socket.socket()
print("Socket Created.")

host = socket.gethostname()
print(host)
port = 1080
s.bind((host, port))

s.listen(3)
print('waiting for connection...')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode
    print('connected successfully,', addr, name)
   
    c.send(bytes('Welcome to Niama', 'utf-8'))
 
    c.close()

