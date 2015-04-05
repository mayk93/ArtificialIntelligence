"""
The network client is started by the UI client
application.
The network client looks for a file called recording.
When it finds this file, it sends it to the server.
It than deletes the file.
"""

#Libraries
import socket
import sys
import os

#Variables
verbose = True
recordingName = "recording.wav"
recordingExists = os.path.exists(recordingName)
HOST = "104.155.13.116" #This is the Google Cloud compute engine VM instance IP
PORT = 5555
MAX_SIZE = 1024
GoogleCloudServer = (HOST,PORT)
clientSocket = socket.socket() #This is a default, TCP socket

#Script
if verbose: print("Starting connection.")
clientSocket.connect(GoogleCloudServer)
if verbose: print("Looking for recording.")

while not recordingExists:
    recordingExists = os.path.exists(recordingName)

if verbose: print("Recording found. Sending to server for processing.")

recording=open (recordingName,"rb") #Open a stream to the recording
partialRecording = recording.read(MAX_SIZE) #1024 bytes out of the whole recording

while partialRecording:
    clientSocket.send(partialRecording)
    partialRecording = recording.read(MAX_SIZE)

if verbose: print("Recording sent. Waiting for confirmation.")
confirmation = clientSocket.recv(MAX_SIZE)
confirmation = confirmation.decode()
if verbose: print("Decoding confirmation.")
while confirmation != SAVED:
    pass
if verbose: print("Confirmation received. Deleting recording.")
os.remove(recordingName)
if verbose: print("Recording deleted. Closing socket.")
clientSocket.close()
if verbose: print("Socket closed.")
