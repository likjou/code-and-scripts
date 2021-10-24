import http.client

print('This program returns all the possible headers to send to a web server')

host =input("Please enter a IP address to connect to:")
port =input("please enter a port to connect to(default:80):")

if port == "":
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('OPTIONS','/')
    response = connection.getresponse()
    print("Enable Methods are:",response.getheader('allow'))
    connection.close()
except ConnectionRefusedError:
    print("connection failed")