#Libraries
import speech_recognition as SpeechRecognition
import socket
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
    with microphone as source:
        audio = recognizer.listen(source)
    return audio
def getText(sound):
    try:
        return recognizer.recognize(sound)
    except LookupError:
        return RECOGNITION_ERROR
def displayText(text):
    print("Output: ",text)
def sendText(text):
    clientSocket.sendto(text.encode('utf-8'), GoogleCloud)
def getServerText():
    while True:
        try:
            (reply,address) = clientSocket.recvfrom(MAX_SIZE)
            print('Server reply : ' + reply.decode('utf-8'))
        except socket.error as msg:
            print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()
def main():
    sendText(getText(getSound()))
    getServerText()
if __name__=='__main__':
    main()
