#Libraries
import socket
import threading
import os

#Variables
LOCAL_HOST = '127.0.0.1'
GCE_SERVER = '104.155.2.110'
DEFAULT_PORT = 5000
MAX_SIZE = 1024
QUIT = 'q'
YES = 'Y'
NO = 'n'

#Functions
def process(data):
    exists = data[:6]
    print(exists.decode("utf-8"))
    return exists.decode("utf-8")

def getSize(data):
    return data[6:].decode("utf-8")

def setup():
    host = LOCAL_HOST
    port = DEFAULT_PORT
    clientSocket = socket.socket()
    clientSocket.connect((host,port))
    fileName = input("File Name ->")
    if fileName != QUIT:
        clientSocket.send(bytes(fileName, "utf-8"))
        data = clientSocket.recv(MAX_SIZE)
        exists = process(data)
        print("Ex:",exists)
        if str(exists) == 'EXISTS':
            fileSize = int(getSize(data))
            download = input("Download? (Y/n) ->")
            if download == YES:
                clientSocket.send(bytes('OK', "utf-8"))
                file = open('new_'+fileName,'wb')
                data = clientSocket.recv(MAX_SIZE)
                totalReceived = len(data)
                file.write(data)
                while totalReceived < fileSize:
                    data = clientSocket.recv(MAX_SIZE)
                    totalReceived += len(data)
                    file.write(data)
                    print("{0:.2f}".format(totalReceived/float(fileSize)*100),"% - Downloaded")
                print("Download Complete")
        else:
            print("File does not exist.")
    clientSocket.close()

#Main
def main():
    setup()
if __name__ == '__main__':
    main()
