#command list
#view_cwd - will show current workning directory
#custom_dir - to view custom directory
#download_files - to download files remotely

import socket
import os

c = socket.socket()
print("socket created...")


host = input("Please input an address to connect:")
port = 9999

c.connect((host, port))
print("connecting....")

while 1:
    command = input('message:')

    if command == "view_cwd":
        c.send(command.encode())
        print('command sent.')
        c.recv(1024)
        print('command being processed.')
        files = c.recv(5000)
        files = files.decode()
        print('command output:', files)

    elif command == "custom_dir":
        user_input = input("Custom Dir:")
        c.send(command.encode())
        c.send(user_input.encode())
        print('command sent.')
        files = c.recv(5000)
        files = files.decode()
        print("List of Dir:", files)

    elif command == "read_file":
        c.send(command.encode())
        file_path = input("File path including the file name:")
        c.send(file_path.encode())
        data = c.recv(100000)
        data = data.decode()
        print("content of file:", data)

    elif (command == 'q' or command == 'Q'):
        c.send('q'.encode())
        c.close()
        print("closing connection...")
        break;

    else:
        c.send(command.encode())
        print('message sent.')



