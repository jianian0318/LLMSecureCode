import socket
import ssl

def connect(host, port):
    """
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as parameter.
    Then, return the socket.
    """
    # Create a raw socket
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Specify SSL version to be used
    context = ssl.create_default_context()

    # Wrap the raw socket with SSL
    ssl_socket = context.wrap_socket(raw_socket, server_hostname=host)

    # Connect to host and port
    ssl_socket.connect((host, port))

    return ssl_socket