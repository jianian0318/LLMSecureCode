import socket
import ssl

def connect(host, port):
    '''
    Create a client SSL socket that uses the latest secure SSL/TLS version,
    and connect to the socket on the host and port provided as parameter.
    Then, return the socket.
    '''
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_2
    ssl_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM),
                                     server_hostname=host)
    ssl_socket.connect((host, port))
    
    return ssl_socket