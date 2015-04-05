import socket
import sys

HOST = "104.155.13.116"
PORT = 5555
s = socket.socket()

print("Connecting ...")

s.connect((HOST,PORT))

print("Connected. Now, reading file")

f=open ("recording.wav", "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
s.close()
