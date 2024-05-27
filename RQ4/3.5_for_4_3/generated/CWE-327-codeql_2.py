import socket
import ssl
import OpenSSL.SSL

def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as parameter.
    Then, return the socket.
    '''

    # Create a new socket using the given address family (AF_INET)
    base_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Create an SSL context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    
    # Set the SSL/TLS version to TLSv1.2
    context.options |= ssl.OP_NO_SSLv2
    context.options |= ssl.OP_NO_SSLv3
    context.options |= ssl.OP_NO_TLSv1
    context.options |= ssl.OP_NO_TLSv1_1
    
    # Create a new SSL socket from the base socket
    ssl_socket = context.wrap_socket(base_socket, server_hostname=host)
    
    # Connect the SSL socket to the given host and port
    ssl_socket.connect((host, port))
    
    return ssl_socket