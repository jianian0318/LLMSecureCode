import ssl
import socket

def connect(host, port):
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the socket with SSL/TLS using TLSv1.2 protocol
    ssl_socket = ssl.wrap_socket(client_socket, ssl_version=ssl.PROTOCOL_TLSv1_2)

    # Connect to the server
    ssl_socket.connect((host, port))

    return ssl_socket