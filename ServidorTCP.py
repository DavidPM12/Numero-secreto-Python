import socket 
import random

HOST="127.0.0.1"
PORT=2000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
num=random.randint(1,10)
s.listen()
conn,addr=s.accept()
print(f"Conexion con el cliente IP({addr}) Puerto({addr[1]})")  
while True:
    data=conn.recv(1024)
    if num==int(data.decode()):
        conn.send("HAS GANADO".encode())
        conn.close()
    else: 
        if num>int(data.decode()):
            conn.send("EL NUMERO ES MAYOR AL QUE HAS DADO".encode())
        else:
            conn.send("EL NUMERO ES MENOR AL QUE HAS DADO".encode())
