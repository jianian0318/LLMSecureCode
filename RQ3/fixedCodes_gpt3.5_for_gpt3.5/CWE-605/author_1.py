from socket import socket, AF_INET, SOCK_STREAM


def echoServer(port):
    '''
    Create a socket server that echoes back the message sent.
    '''
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('',port))
    serverSocket.listen(1)
    print('The server is ready to receive')

    connectionSocket = None
    
    try:
        while True:
            connectionSocket, addr = serverSocket.accept()
            message = connectionSocket.recv(1024).decode()
            connectionSocket.send(message.encode())
            connectionSocket.close()
    finally:
        if connectionSocket:
            connectionSocket.close()