import socket

LOCAL_HOST = '127.0.0.1'
GCE_SERVER = '104.155.2.110'
DEFAULT_PORT = 5000
MAX_SIZE = 1024

def main():
    host = LOCAL_HOST
    port = DEFAULT_PORT

    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    serverSocket.bind((host,port))
    print("Server Started.")

    while True:
        data, address = serverSocket.recvfrom(MAX_SIZE)
        print("From:",str(address))
        print("Data:",str(data))
        data = str(data).upper()
        toSendData = bytes(data, "utf-8")
        serverSocket.sendto(data,address)
    serverSocket.close()

if __name__ == '__main__':
    main()
