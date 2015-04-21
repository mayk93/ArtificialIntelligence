#Libraries
import speech_recognition as SpeechRecognition
import socket
import pickle
import threading
import sys
#Instantiation Methods
def createUDPSocket():
    try:
        newSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return newSocket
    except socket.error:
        print('Failed to create socket.')
        return None
#Variables
clientSocket = createUDPSocket()
HOST = '104.155.13.116'
PORT = 5555
splitLenght = 100
redundancySending = 10
GoogleCloud = (HOST,PORT)

recognizer = SpeechRecognition.Recognizer()
recognizer.energy_threshold = 1500
microphone = SpeechRecognition.Microphone()

RECOGNITION_ERROR = "Could not understand audio."
MAX_SIZE = 1024
#Functions
def split(picklestring,size):
    return [picklestring[i:i+size] for i in range(0, len(picklestring), size)]
def displayText(text):
    print("Output: ",text)
def getSound():
    print("Get Sound Method.")
    with microphone as source:
        audio = recognizer.listen(source)
    print("End Get Sound Method.")
    return audio
def sendSound(sound):
    picklestring = pickle.dumps(sound)
    picklestring += "!".encode('utf-8')
    smallPickleStringsArray = split(picklestring,splitLenght)
    for index,smallPickleString in enumerate(smallPickleStringsArray):
        print("Sending package:",index)
        for sendManyTimes in range(0,redundancySending):
            package = str(index).encode('utf-8') + "#".encode('utf-8') + smallPickleString
            clientSocket.sendto(package,GoogleCloud)
    '''
    print("Pickled String:",picklestring)
    while True:
        clientSocket.sendto(picklestring,GoogleCloud)
    '''
def getServerText():
    while True:
        try:
            (reply,address) = clientSocket.recvfrom(MAX_SIZE)
            print('Server reply : ' + reply.decode('utf-8'))
        except socket.error as msg:
            print("No or bad reply.")
            try:
                print("Reply:",reply)
                print("Address:",address)
            except:
                pass
            pass
def main():
    print("Getting and sending sound sound.")
    #sendSound(getSound())
    audio = getSound()
    threading.Thread(target=sendSound,args=(audio,)).start()
    print("Got and sent sound.")
    threading.Thread(target=getServerText).start()
    #getServerText()
    print("Ending main.")
if __name__=='__main__':
    main()
