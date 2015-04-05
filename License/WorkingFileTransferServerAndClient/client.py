import socket
import sys

HOST = "104.155.13.116"
PORT = 80

s = socket.socket()
s.connect((HOST,PORT))
f=open ("recording.wav", "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
s.close()
