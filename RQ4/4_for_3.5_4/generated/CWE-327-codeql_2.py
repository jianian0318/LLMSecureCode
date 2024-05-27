import socket
import ssl

def connect(host, port):
    # Create a client SSL socket with a secure configuration
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    
    # Enforce the use of TLS 1.2 or higher
    context.options |= ssl.OP_NO_SSLv2
    context.options |= ssl.OP_NO_SSLv3
    context.options |= ssl.OP_NO_TLSv1
    # Use of TLSv1.1 can be disabled to be even more secure:
    context.options |= ssl.OP_NO_TLSv1_1

    # Optionally, configure the server_hostname for SNI (Server Name Indication)
    client_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=host)

    # Connect to the socket on the host and port provided
    client_socket.connect((host, port))

    return client_socket