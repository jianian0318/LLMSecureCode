import socket
import ssl

def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as parameter.
    '''
    # Create an SSL context for the socket
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # Set the minimum SSL/TLS version to TLSv1.2
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    # Disable insecure SSL/TLS versions
    context.options |= ssl.OP_NO_SSLv2
    context.options |= ssl.OP_NO_SSLv3
    context.options |= ssl.OP_NO_TLSv1
    # Create a TCP socket using IPV4
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Wrap the socket with SSL
    ssl_sock = context.wrap_socket(sock, server_hostname=host)
    # Connect to the server
    ssl_sock.connect((host, port))
    return ssl_sock