#Libraries
import socket
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
MAX_SIZE = 2048
GoogleCloud = (HOST,PORT)
serverSocket = createUDPSocket()
bindSocket(serverSocket,GoogleCloud)
#Function
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
def main():
    getTextFromClient()
if __name__=='__main__':
    main()
