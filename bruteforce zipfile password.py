from zipfile import ZipFile
from string import digits
import itertools

brute = itertools.product(digits,repeat =5)
with ZipFile ("00000012.zip") as zf:
    for i in brute:
        i = ''.join(i)
        password = "ctflag"+i
        try:
            zf.extracall(pwd=bytes(password,'utf-8'))
            print("[+] password is "+password)
        except:
            pass
