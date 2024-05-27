import socket
import ssl

def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as parameter.
    Then, return the socket.
    '''
    # Create a client socket that uses IPV4 and the TCP protocol
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the context for the SSL with specific protocol
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

    # Wrap the socket with SSL
    client_socket = context.wrap_socket(client_socket, server_hostname=host)

    # Connect to the socket on the host and port provided
    client_socket.connect((host, port))

    # Return the socket
    return client_socket