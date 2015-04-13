#Libraries
import speech_recognition as SpeechRecognition
import socket
import pickle
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
GoogleCloud = (HOST,PORT)

recognizer = SpeechRecognition.Recognizer()
recognizer.energy_threshold = 1500
microphone = SpeechRecognition.Microphone()

RECOGNITION_ERROR = "Could not understand audio."
MAX_SIZE = 2048
#Functions
def getSound():
    print("Get Sound Method.")
    with microphone as source:
        audio = recognizer.listen(source)
    print("End Get Sound Method.")
    return audio
'''
def getText(sound):
    try:
        return recognizer.recognize(sound)
    except LookupError:
        return RECOGNITION_ERROR
'''
def displayText(text):
    print("Output: ",text)
'''
def sendText(text):
    clientSocket.sendto(text.encode('utf-8'), GoogleCloud)
'''
def sendSound(sound):
    print("Sending test string 0")
    clientSocket.sendto("Test 0".encode('utf-8'),GoogleCloud)
    print("Send Sound Method.")
    picklestring = pickle.dumps(sound)
    clientSocket.sendto(picklestring,GoogleCloud)
    print("Sending test string 1")
    clientSocket.sendto("Test 1".encode('utf-8'),GoogleCloud)
    print("End Send Sound Method.")
def getServerText():
    while True:
        try:
            (reply,address) = clientSocket.recvfrom(MAX_SIZE)
            print('Server reply : ' + reply.decode('utf-8'))
        except socket.error as msg:
            print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()
def main():
    #sendText(getText(getSound()))
    print("Getting and sending sound sound.")
    sendSound(getSound())
    print("Got and sent sound.")
    getServerText()
    print("Ending main.")
if __name__=='__main__':
    main()
