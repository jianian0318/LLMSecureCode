import socket
import ssl


def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as parameter.
    Then, return the socket.
    '''
    # Create an SSL context for the socket
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # Create a TCP socket using IPV4
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Wrap the socket with SSL
    ssl_sock = context.wrap_socket(sock)
    # Connect to the server
    ssl_sock.connect((host, port))
    return ssl_sock