import socket
import ssl

def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as parameter.
    Then, return the socket.
    '''
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Use SSL/TLS best practices by creating SSL context with secure settings
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    
    # Wrap the socket object with SSL using the secure context
    ssl_sock = context.wrap_socket(sock, server_hostname=host)
    
    # Connect to the host and port
    ssl_sock.connect((host, port))
    
    # Return the SSL/TLS socket
    return ssl_sock