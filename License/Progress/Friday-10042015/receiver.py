# ----- RECEIVER -----

#from socket import *
import socket
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


"""
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
    received = clientSocket.recvfrom(MAX_SIZE)
    print("Received")
    if condition:
        print("Starting translation with arguments:",received)
        os.system("translate.py")
        condition = False
"""

'''
    Simple udp socket server
'''
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5555 # Arbitrary non-privileged port
 
# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket created')
except socket.error as msg :
    print('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
 
 
# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print('Socket bind complete')
 
#now keep talking with the client
while True:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    d = d.decode('utf-8')
    data = d[0]
    addr = d[1]
    print("Received data.")
    if not data:
        print("Stopped receiving data.") 
        break
     
    reply = "Starting translation with arguments:"
    print("Starting translation with arguments:",data)
    #os.system("~/var/www/translate.py")
    #execfile("translate.py")
    exec(open("translate.py").read())
     
    s.sendto(reply.encode('utf-8') , addr)
    print('Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip())
     
s.close()
