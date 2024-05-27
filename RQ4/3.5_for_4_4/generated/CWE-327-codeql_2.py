import socket
import ssl

def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as parameter.
    Then, return the socket.
    '''

    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the SSL/TLS version
    ssl_version = ssl.PROTOCOL_TLS  # Use TLS 1.2 as the default protocol (or choose the appropriate version)

    # Wrap the socket for SSL
    ssl_sock = ssl.wrap_socket(sock, ssl_version=ssl_version)

    # Connect to the given host and port
    ssl_sock.connect((host, port))

    # Return the ssl wrapped socket
    return ssl_sock