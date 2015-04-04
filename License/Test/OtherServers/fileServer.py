'''
File Server
'''
#Libraries
import socket
import threading
import os

#Variables
LOCAL_HOST = '127.0.0.1'
GCE_SERVER = '104.155.2.110'
DEFAULT_PORT = 5000
MAX_SIZE = 1024

#Functions
def RetrieveFile(name,fileSocket):
    fileName = fileSocket.recv(MAX_SIZE)
    print("Requested file:",fileName)
    if os.path.isfile(fileName):
        print("Requested file IN:",fileName)
        fileSocket.send(bytes( ("EXISTS"+str(os.path.getsize(fileName))) , "utf-8"))
        userResponse = fileSocket.recv(MAX_SIZE)
        if userResponse[:2].decode("utf-8") == 'OK':
            with open(fileName,'rb') as file:
                bytesToSend = file.read(MAX_SIZE)
                fileSocket.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = file.read(MAX_SIZE)
                    fileSocket.send(bytesToSend)
    else:
        fileSocket.send(bytes("ERROR", "utf-8")) #bytes("ERROR", "utf-8")
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
        thread = threading.Thread(target=RetrieveFile,args=("retrieveThread",connection))
        thread.start()
    serverSocket.close()

#Main
def main():
    setup()
if __name__ == '__main__':
    main()
