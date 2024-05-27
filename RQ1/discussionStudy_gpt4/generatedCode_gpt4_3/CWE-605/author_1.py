import socket

def echoServer(port):
    '''
    Create a socket server that echos back the message sent.
    '''
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', port)
    
    # Bind the socket to the port
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    
    while True:
        # Wait for a connection
        print('waiting for a connection')
        client_socket, client_address = server_socket.accept()
        
        try:
            print('connection from', client_address)
            
            # Receive and send back the data
            while True:
                data = client_socket.recv(16)
                print('received {!r}'.format(data))
                if data:
                    print('sending data back to the client')
                    client_socket.sendall(data)
                else:
                    print('no data from', client_address)
                    break
                
        finally:
            # Clean up the connection
            client_socket.close()

echoServer(8080)