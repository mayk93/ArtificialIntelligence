# ----- SENDER ------

from socket import *
import sys
import time
import os

'''
s = socket(AF_INET,SOCK_DGRAM)
host = "104.155.13.116"
port = 5555
buf = 2048
addr = (host,port)

file_name = "recording.wav"
print("Sending file name.")
s.sendto(file_name,addr)
print("Sent file name.")
f=open(file_name,"rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print("Sending.")
        data = f.read(buf)
        print("Sent.")
        time.sleep(1)
        print("Slept.")
s.close()
f.close()
'''

HOST = "104.155.13.116" #This is the Google Cloud compute engine VM instance IP
PORT = 5555
GOOGLE_CLOUD = (HOST,PORT)
MAX_SIZE = 2048

filePath = "recording.wav"
filebject = open(filePath, "rb")
fileSize = os.path.getsize(filePath)

#An UDP socket
serverSocket = socket(AF_INET,SOCK_DGRAM)

fileData = filebject.read(MAX_SIZE)
while fileData:
    print("Sending.")
    transmisionResult = serverSocket.sendto(fileData,GOOGLE_CLOUD)
    print("Transmision result: ",transmisionResult)
    fileData = filebject.read(MAX_SIZE)
    print("Sent.")
    print("Sleep.")
    time.sleep(1)
    print("Sleep over.")
    
