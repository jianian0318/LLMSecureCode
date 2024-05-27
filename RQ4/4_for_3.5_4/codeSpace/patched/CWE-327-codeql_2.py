import socket
import ssl

def connect(host, port):
    # Create a client SSL socket
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    client_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

    # Connect to the socket on the host and port provided
    client_socket.connect((host, port))

    return client_socket