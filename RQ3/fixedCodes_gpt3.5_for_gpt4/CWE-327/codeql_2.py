import socket
import ssl

def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as a parameter.
    Then, return the socket.
    '''
    # Create a standard socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the socket in SSL using a secure protocol
    ssl_sock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLS)

    # Connect the socket to the host on the provided port
    ssl_sock.connect((host, port))

    # Finally, return the SSL socket
    return ssl_sock