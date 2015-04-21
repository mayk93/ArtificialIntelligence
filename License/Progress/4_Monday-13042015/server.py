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
MAX_SIZE = 1024
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
    maxPackageReceived = -1
    audioPicklestring = ""
    while True:
        print("In while.")
        (received,address) = serverSocket.recvfrom(MAX_SIZE)
        print("Received.")
        #try:
        '''
        print("In try.")
        print("Raw received:",received)
        print("Deserialized received:",pickle.load(received))
        '''
        receivedPackageIndexByte = str(pickle.loads(received)).split('#', 1)[0]
        receivedPackageIndex = str(receivedPackageIndexByte)
        print("Received package:" , receivedPackageIndex)
        if int(str(receivedPackageIndex)) > maxPackageReceived and "!".encode('utf-8') not in received:
            print("Appending package ",receivedPackageIndex)
            audioPicklestring += str(received).split("#",1)[1]
        if int(str(receivedPackageIndex)) > maxPackageReceived and "!".encode('utf-8') in received:
            print("Final package received.")

            receivedNoIndex = str(received).split("#",1)[1]
            receivedNoEndToken = str(receivedNoIndex).split("!",1)[0]
            audioPicklestring += receivedNoEndToken

            audio = pickle.loads(audioPicklestring)
            print("Received data. Sending data to processing.")
            text = recognizeAudio(audio)
            print("Received text from audio recognition.")

            reply = "Starting translation with arguments: " + text
            print("Starting translation with arguments:",text)
            exec(open("translate.py").read())
            serverSocket.sendto(reply.encode('utf-8') , address )
            print('Message[' + address[0] + ':' + str(address[1]) + '] - ' + text.strip())
        else:
            reply = "Received " + str(maxPackageReceived) + " packages. Waiting for more."
            print("Starting translation with arguments:",text)
            exec(open("translate.py").read())
            serverSocket.sendto(reply.encode('utf-8') , address )
            print('Message[' + address[0] + ':' + str(address[1]) + '] - ' + text.strip())
        #except:
            '''
            print("In except.")
            pass
            '''
        if not received:
            print("Stopped receiving data.")
            break
    serverSocket.close()
def main():
    getSoundFromClient()
if __name__=='__main__':
    main()
