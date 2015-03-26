'''
Upload Client
'''
#Libraries
import socket
import os

#Variables
LOCAL_HOST = '127.0.0.1'
GCE_SERVER = '104.155.2.110'
DEFAULT_PORT = 5000
MAX_SIZE = 1024
DEFAULT_FILE_NAME = 'recording.wav'
QUIT = 'q'
YES = 'Y'
NO = 'n'

#Functions
def exists(fileName):
    if os.path.isfile(fileName):
        return true
    return false
def getSize(fileobject):
    fileobject.seek(0,2)
    size = fileobject.tell()
    return size
def setup():
    host = GCE_SERVER
    port = DEFAULT_PORT
    clientSocket = socket.socket()
    clientSocket.connect((host,port))

    '''
    I don't input, it automaticly sends the file once recorded
    '''
    #fileName = input("File to upload ->")
    fileName = DEFAULT_FILE_NAME
    while not exists(fileName):
        pass #Waiting for the file to "appear"

    #print("To send:",fileName)
    #print("Sending file name.")
    clientSocket.send(bytes( str(fileName) , "utf-8"))
    #print("Sent file name.")
    if fileName != QUIT:
        if os.path.isfile(fileName): #This check is now redundant because of exists method. Will be refactored

            #print("Opening file.")
            file = open(fileName,'rb')
            #print("File opened.")

            #print("Sending file size.")
            fileSize = int(getSize(file))
            clientSocket.send(bytes( str(fileSize) , "utf-8"))
            #print("File size:",fileSize)

            #print("Sending.")
            with open(fileName,'rb') as file:
                bytesToSend = file.read(MAX_SIZE)
                clientSocket.send(bytesToSend)
                #print("Sent initial data")
                while bytesToSend != "":
                    bytesToSend = file.read(MAX_SIZE)
                    clientSocket.send(bytesToSend)
                    #print("Sent additional data")
            #print("Sent!")
        else:
            #print("File does not exist.")
    clientSocket.close()
#Main
def main():
    setup()
if __name__ == '__main__':
    main()
# C:\Users\initial\Documents\University\College\License\Test
