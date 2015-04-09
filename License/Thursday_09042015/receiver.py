# ----- RECEIVER -----

from socket import *
import sys
import select
import pyglet
import time
import os
'''
host="0.0.0.0"
port = 5555
s = socket(AF_INET,SOCK_DGRAM)

print("Binding.")
s.bind((host,port))

addr = (host,port)
buf = 2048

print("Receiving.")
data,addr = s.recvfrom(buf)
print("Received File:",data.strip())
f = open(data.strip(),'wb')

data,addr = s.recvfrom(buf)
print("Enter try.")
try:
    print("Try. Downloading.")
    while(data):
        f.write(data)
        s.settimeout(2)
        data,addr = s.recvfrom(buf)
except timeout:
    f.close()
    s.close()
    print("File Downloaded.")
    os.system("translate.py")
    print("Translation launched.")
'''

HOST = "" #This is the Google Cloud compute engine VM instance IP
PORT = 5555
GOOGLE_CLOUD = (HOST,PORT)
MAX_SIZE = 2048

clientSocket = socket(AF_INET,SOCK_DGRAM)
print("Binding")
clientSocket.bind(GOOGLE_CLOUD)
print("Bound")

condition = True

while True:
    print("Receiving.")
    received = clientSocket.recv(MAX_SIZE)
    print("Received")
    if condition:
        print("Starting translation with arguments:",received)
        os.system("translate.py")
        condition = False
