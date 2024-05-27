import socket
import ssl

def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as parameter.
    Then, return the socket.
    '''
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Wrap the socket with SSL
    ssl_socket = ssl.wrap_socket(client_socket)
    
    # Connect to the server
    ssl_socket.connect((host, port))
    
    # Return the socket
    return ssl_socket