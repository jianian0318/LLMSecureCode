import socket
import ssl

def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as parameter.
    Then, return the socket.
    '''
    # Create a standard socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

    # Wrap the socket in SSL
    ssl_sock = context.wrap_socket(sock)

    # Connect the socket to the host on the provided port
    ssl_sock.connect((host, port))

    # Finally, return the SSL socket
    return ssl_sock