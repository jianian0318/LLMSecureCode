def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as parameter.
    Then, return the socket.
    '''
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
    # Wrap the socket with SSL
    ssl_sock = ssl.wrap_socket(sock)

    # Connect to the host and port
    ssl_sock.connect((host, port))

    return ssl_sock