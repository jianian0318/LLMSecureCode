from socket import socket


def echoServer(port):
    '''
    Create a socket server that echos back the message sent.
    '''
    # Create a socket object
    server_socket = socket()

    # Bind the socket to a local address and port
    server_socket.bind(('localhost', port))

    # Listen for incoming connections
    server_socket.listen(1)

    while True:
        # Accept a connection
        connection, address = server_socket.accept()

        try:
            # Receive data from the client
            data = connection.recv(1024)

            # Echo back the data to the client
            connection.sendall(data)
        finally:
            # Close the connection
            connection.close()
