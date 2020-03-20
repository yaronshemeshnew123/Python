import socket
s = socket.socket()
host = socket.gethostname()
port = 8090
s.bind((host,port))
s.listen(1) #one computer
print(host)
print ("waiting for any incoming connections....")
conn, addr = s.accept()
print(addr,"Has connected to the server")

filename=input (str("please enter the filename of the file:"))
file= open(filename,'rb')
file_data= file.read(1024)
conn.send(file_data)
print("Data has been transmitted successfully")

