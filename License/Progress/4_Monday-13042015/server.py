#Libraries
import socket
import pickle
import speech_recognition as SpeechRecognition
#Instantiation Methods
def createUDPSocket():
    try:
        newSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return newSocket
    except socket.error:
        print('Failed to create socket.')
        return None
def bindSocket(socket,destination):
    try:
        socket.bind(destination)
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()
#Variables
HOST = ''
PORT = 5555
MAX_SIZE = 4096
RECOGNITION_ERROR = "Could not understand audio."
GoogleCloud = (HOST,PORT)
serverSocket = createUDPSocket()
bindSocket(serverSocket,GoogleCloud)
#Function
'''
def getTextFromClient():
    print("Waiting for data.")
    while True:
        (rawText,address) = serverSocket.recvfrom(MAX_SIZE)
        text = rawText.decode('utf-8')
        print("Received data.")
        if not rawText:
            print("Stopped receiving data.")
            break
        reply = "Starting translation with arguments:"
        print("Starting translation with arguments:",text)
        exec(open("translate.py").read())
        serverSocket.sendto(reply.encode('utf-8') , address )
        print('Message[' + address[0] + ':' + str(address[1]) + '] - ' + text.strip())
    serverSocket.close()
'''
def recognizeAudio(audio):
    try:
        return recognizer.recognize(sound)
    except LookupError:
        return RECOGNITION_ERROR
def getSoundFromClient():
    print("Waiting for data.")
    while True:
        (received,address) = serverSocket.recvfrom(MAX_SIZE)
        try:
            pickledAudio = received
            audio = pickle.load(pickledAudio)
            print("Received data. Sending data to processing.")
            text = recognizeAudio(audio)
            print("Received text from audio recognition.")

            reply = "Starting translation with arguments: " + text
            print("Starting translation with arguments:",text)
            exec(open("translate.py").read())
            serverSocket.sendto(reply.encode('utf-8') , address )
            print('Message[' + address[0] + ':' + str(address[1]) + '] - ' + text.strip())

        except:
            encodedText = received
            text = encodedText.decode('utf-8')
            print("Received text:",text)
        if not received:
            print("Stopped receiving data.")
            break
    serverSocket.close()
def main():
    getSoundFromClient()
if __name__=='__main__':
    main()
