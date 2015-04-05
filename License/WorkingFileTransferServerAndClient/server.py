import socket
import sys
s = socket.socket()

HOST = "104.155.13.116"
PORT = 80

s.bind((HOST,PORT))
s.listen(10)

while True:
    sc, address = s.accept()

    print(address)
    i=1
    f = open('file_'+ str(i)+".wav",'wb') #open in binary
    i=i+1
    while (True):
        l = sc.recv(1024)
        while (l):
                f.write(l)
                l = sc.recv(1024)
    f.close()


    sc.close()

s.close()
