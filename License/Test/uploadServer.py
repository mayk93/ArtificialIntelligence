'''
Upload Server
'''
#Libraries
import socket
import threading
import os

#Variables
LOCAL_HOST = '127.0.0.1'
GCE_SERVER = '104.155.2.110'
DEFAULT_PORT = 5765
MAX_SIZE = 1024

#Functions
def goodFileName(fileName):
    if fileName != "" and fileName != None:
        return True
    return False
def SaveFile(name,fileSocket):
    print("The save thread.")
    fileName = fileSocket.recv(MAX_SIZE)
    print("To save file:",fileName)
    if goodFileName(fileName):
        print("Getting file size.")
        fileSize = int((fileSocket.recv(MAX_SIZE)).decode("utf-8"))
        print("File size:",fileSize)
        print("Saving:",fileName.decode("utf-8"),"with size",fileSize)
        file = open(fileName.decode("utf-8"),'wb')
        print("Created file.")
        data = fileSocket.recv(MAX_SIZE)
        print("Received initial data.")
        totalReceived = len(data)
        print("Downloading file. Received",totalReceived,"out of",fileSize)
        file.write(data)
        while totalReceived < fileSize:
            data = fileSocket.recv(MAX_SIZE)
            totalReceived += len(data)
            file.write(data)
            print("{0:.2f}".format(totalReceived/float(fileSize)*100),"% - Downloaded")
        print("Download complete.")
    fileSocket.close()
def setup():
    host = LOCAL_HOST
    port = DEFAULT_PORT
    serverSocket = socket.socket()
    serverSocket.bind((host,port))
    serverSocket.listen(5)
    print("Server Started.")
    while True:
        connection , address = serverSocket.accept()
        print("Client IP:",str(address))
        thread = threading.Thread(target=SaveFile,args=("retrieveThread",connection))
        thread.start()
    serverSocket.close()
#Main
def main():
    setup()
if __name__ == '__main__':
    main()
