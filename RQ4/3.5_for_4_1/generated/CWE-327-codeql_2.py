import socket
import ssl

def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as parameter.
    Then, return the socket.
    '''
    # Create a standard socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap socket with SSL using TLSv1.2
    ssl_sock = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1_2)

    # Connect to host
    ssl_sock.connect((host, port))

    return ssl_sock