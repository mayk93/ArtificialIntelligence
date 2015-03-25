import socket

LOCAL_HOST = '127.0.0.1'
GCE_SERVER = '104.155.2.110'
DEFAULT_PORT = 5000
MAX_SIZE = 1024

def main():
    host = LOCAL_HOST
    port = DEFAULT_PORT

    serverSocket = socket.socket()
    serverSocket.bind((host,port))
    serverSocket.listen(1)
    connection , address = serverSocket.accept()

    print("IP:",str(address))

    while True:
        data = connection.recv(MAX_SIZE)
        if not data:
            break
        print("Received data:",str(data))
        data = str(data).upper()
        toSendData = bytes(data, "utf-8")
        print("Sending:",str(data))
        connection.send(toSendData)
    connection.close()

if __name__ == '__main__':
    main()
