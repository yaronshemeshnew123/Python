import socket
s=socket.socket()
host=input(str("please enter the host address of the sender:"))
port= 8090
s.connect((host,port))
print("Connected ...")

filename = input(str("please enter a filename for the incoming file:"))
file = open (filename,'wb')
file_data = s.recv (1024)
file.write (file_data)
file.close ()
print ("File has been received successfully.")
