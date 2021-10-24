import os

files = os.listdir("C:/Users/likjo/Desktop/ctf/ctff")

#for printing ctf/ctff/
for file in files:
    fileDir = 'C:/Users/likjo/Desktop/ctf/ctff/'
    print("current path:", fileDir)
    if len(os.listdir(fileDir + file)) == 0:
        print("file " + file + " is empty")
    else:
        print("file " + file + " is not empty")

# for printing folders inside ctf/ctff/
print("---------------------------------------------")
for file in files:
     #now in ctf/ctff/(here)
    for f in file:    
        #for every folder in ctf/ctff/(folder)
        fileDir = 'C:/Users/likjo/Desktop/ctf/ctff/'+ file +"/"
        if len(os.listdir(fileDir + file)) == 0:
            print("subfile " + file + " is empty")
        else:
            print("subfile " + file + " is not empty")
