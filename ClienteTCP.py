import socket
import random

HOST="127.0.0.1"
PORT=2000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
i=0
ganar=True
while i!=4 and ganar:
    num=input("Dame un numero ")
    i=i+1
    s.send(num.encode())
    data=s.recv(1024)
    if data.decode()=="HAS GANADO":
        print("HAS ACERTADO")
        ganar=False
    else:
        print(f"Recibo: {data.decode()}")
s.close
