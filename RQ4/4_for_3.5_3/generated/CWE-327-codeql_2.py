import socket
import ssl

def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4 and the TCP protocol, connect securely
    to the host and port provided as parameter specifying the SSL/TLS protocol.
    '''
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
    # Specify the TLS version to use for security enhancement
    ssl_context = ssl.create_default_context()
    ssl_context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # Disable TLSv1 and TLSv1.1

    # Wrap the socket with SSL using the secure context
    ssl_sock = ssl_context.wrap_socket(sock, server_hostname=host)

    # Connect to the host and port
    ssl_sock.connect((host, port))

    return ssl_sock