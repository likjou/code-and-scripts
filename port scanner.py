import socket

target = input("Please Input the target's IP address:")
portRange = input("Please Input the Port Range (ex:5-200):")

lowPort = int(portRange.split("-")[0])
highPort = int(portRange.split("-")[1])

print("scanning host", target, "from port ", lowPort, "to", highPort)

for port in range (lowPort, highPort):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if status == 0:
        print('***Port ',port," - OPEN***")
    else:
        print('Port ',port," - CLOSED")
    s.close()