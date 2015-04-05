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
MAX_SIZE = 2048
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

    recordingSize = int((clientConnection.recv(MAX_SIZE)).decode())
    if verbose: print("Recording size is:",recordingSize)

    recording = open(recordingName,'wb') #Save the recording. Here, recording is a stream to the file, where we write the bytes received via the socket
    if verbose: print("Saving recording.")
    batch = 0
    while (True):
        partialRecording = clientConnection.recv(MAX_SIZE)
        completed = False
        while not completed:
                recording.write(partialRecording) #In the recording file, we write multiple partial recordings in order to get the entire recording.
                if verbose: print("Saving batch:",batch)
                batch += 1
                try:
                    if verbose: print("0. Receiving data from client.")
                    partialRecording = clientConnection.recv(MAX_SIZE)
                    if verbose: print("1. Received data from client.")
                except Exception as e:
                    if verbose: print("Stopped receiving data.")
                    if verbose: print(str(e))
                if os.path.getsize(recordingName) >= recordingSize:
                    completed = True
                if verbose: print("Current recording size:",os.path.getsize(recordingName),"out of",recordingSize)
    recording.close()
    if verbose: print("Recording saved.")
    clientConnection.send(str(SAVED).encode())
    if verbose: print("Confirmation sent.")
    clientConnection.close()
serverSocket.close()
if verbose: print("Socket closed.")
os.system("translate.py")
if verbose: print("NLTK script invoked.")
