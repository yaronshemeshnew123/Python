import socket
import sys
import time

##init ##
f=None
try:
    f=open("status.txt","r")
    filecontent=f.read()

    filecontent=filecontent.split("\n")
    print(filecontent)
except:

    print("file not exists/or found")


finally:
    if f is not None and not f.closed:
        f.close()

port = 65432
ip='127.0.0.1' #local host

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((ip,port))
    for i in filecontent:
        time.sleep(1)
        s.sendall(i.encode())
        data=s.recv(1024)
        print(data)
