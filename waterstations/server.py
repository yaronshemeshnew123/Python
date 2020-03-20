from db import dbconnect
import socket

db=dbconnect("stations.db")
db.connection()



HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)

            recived=data.decode().split(",")
            if len(recived)==3:
                db.insert(recived[0],recived[1],recived[2])


            if data.decode()=="":
                break
            print("Data received from client: ",data.decode())
            conn.sendall(data)
print("finish")
