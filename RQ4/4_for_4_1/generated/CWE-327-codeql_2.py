import socket
import ssl

def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as parameter.
    Then, return the socket.
    '''

    # create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Specify SSL/TLS protocol version
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)  # or whatever protocol version you want
    
    # wrap socket with SSL
    ssl_sock = context.wrap_socket(sock, server_hostname=host)

    # connect to host, port
    ssl_sock.connect((host, port))

    return ssl_sock