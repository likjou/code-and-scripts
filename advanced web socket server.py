import socket #web socket
import platform 
import os 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created...")

host = ''.join(socket.gethostbyname_ex(socket.gethostname())[2][2])
print(host)
port = 9999
s.bind((host,port))

s.listen(3)
print("waiting for connection...")

c, addr = s.accept()
print("connected successfully")

while 1:
    command = c.recv(1024)
    command = command.decode()
    print('message:', command)
    
    if command == "view_cwd":
       files = os.getcwd()
       files = str(files)
       c.send(" ".encode()) 
       c.send(files.encode())
       print('command has been executed successfully.')

    elif command == "custom_dir":
        user_input = c.recv(1024)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        c.send(files.encode())

    elif command == "read_file":
        file_path = c.recv(1024)
        file_path = file_path.decode()
        files = open(file_path,"rb")
        data = files.read()
        c.send(data)
        print("content sent.")

    elif (command == 'q' or command == 'Q'):
        c.recv(1024)
        c.close()
        print("closing connection...")
        break;



    

   

  
