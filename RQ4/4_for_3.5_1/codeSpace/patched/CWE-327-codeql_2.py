import socket
import ssl

def connect(host, port):
    # Create a client SSL socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = ssl.wrap_socket(sock)

    # Connect to the socket on the host and port
    ssl_sock.connect((host, port))

    # Return the socket
    return ssl_sock