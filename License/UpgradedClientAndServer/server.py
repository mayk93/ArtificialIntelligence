'''
The server receives a recording from the network client.
The recordiing is saved in order to be later processed by
the NLTK scrip, called from here, after the recording is saved.
'''

#Libraries
import socket
import sys
import os

#Variables
verbose = True
recordingName = "toTranslate.wav" #The name we save the recording under
recordingExists = os.path.exists(recordingName)
HOST = "" #This is the Google Cloud compute engine VM instance IP
PORT = 5555
MAX_SIZE = 1024
MAX_CONNECTIONS = 10 #For multithreaded refactoring
SAVED = "SAVED"
GoogleCloudServer = (HOST,PORT)
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

#Script
if verbose: print("Binding.")
serverSocket.bind(GoogleCloudServer)
if verbose: print("Bound.")
serverSocket.listen(MAX_CONNECTIONS)
if verbose: print("Listening.")

while True:
    clientConnection, address = serverSocket.accept()
    if verbose: print("Accepted connection from:",address)
    recording = open(recordingName,'wb') #Save the recording. Here, recording is a stream to the file, where we write the bytes received via the socket
    if verbose: print("Saving recording.")
    while (True):
        partialRecording = clientConnection.recv(MAX_SIZE)
        while (partialRecording):
                recording.write(partialRecording) #In the recording file, we write multiple partial recordings in order to get the entire recording.
                partialRecording = clientConnection.recv(MAX_SIZE)
    recording.close()
    if verbose: print("Recording saved.")
    clientConnection.send(str(SAVED).encode())
    clientConnection.close()
serverSocket.close()
if verbose: print("Socket closed.")
os.system("translate.py")
if verbose: print("NLTK script invoked.")
