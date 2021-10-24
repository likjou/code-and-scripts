import requests



credentials = open('uname&passwd.txt', 'r')
for line in credentials :
    # print(credentials.readline())
    payload = {'username':line.strip(),'password':line.strip()}
    print(payload)



req = requests.post("https://httpbin.org/post", data=payload)
res = req.content.decode()
print(res)

