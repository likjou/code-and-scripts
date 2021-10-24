import http.client

print("This program will check a webserver for existing resource.")

host = input('Enter an IP address to connect to:')
port = input('Enter a port to connect to (default:80):')

if port == "":
    port = 80

user_input = input("insert the page that you want to get from web server(ex:/robots.txt): ") 
connection = http.client.HTTPConnection(host,port)
connection.request("GET","/",user_input)

respond = connection.getresponse()
print(respond.status,respond.reason)



