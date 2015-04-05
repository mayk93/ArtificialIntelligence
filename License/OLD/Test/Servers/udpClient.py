import socket

LOCAL_HOST = '127.0.0.1'
GCE_SERVER = '104.155.2.110'
DEFAULT_PORT = 5000
MAX_SIZE = 1024
QUIT = 'q'

def main():
    host = LOCAL_HOST
    port = DEFAULT_PORT + 1 #We are setting up a different server
    server = (LOCAL_HOST,DEFAULT_PORT)

    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    clientSocket.bind((host,port))

    message = input("->")
    toSendMessage = bytes(message, "utf-8")

    while message != QUIT:
        clientSocket.send(toSendMessage)
        data, address = clientSocket.recvfrom(MAX_SIZE)
        print("From:",str(address))
        print("Data:",str(data))
        message = input("->")
        toSendMessage = bytes(message, "utf-8")

if __name__ == '__main__':
    main()
