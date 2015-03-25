import socket

LOCAL_HOST = '127.0.0.1'
GCE_SERVER = '104.155.2.110'
DEFAULT_PORT = 5000
MAX_SIZE = 1024
QUIT = 'q'

def main():
    host = LOCAL_HOST
    port = DEFAULT_PORT

    clientSocket = socket.socket()
    clientSocket.connect((host,port))

    message = input("->")
    toSendMessage = bytes(message, "utf-8")

    while message != QUIT:
        clientSocket.send(toSendMessage)
        data = clientSocket.recv(MAX_SIZE)
        print("Received from server: " + str(data))
        message = input("->")
        toSendMessage = bytes(message, "utf-8")
    clientSocket.close()

if __name__ == '__main__':
    main()
