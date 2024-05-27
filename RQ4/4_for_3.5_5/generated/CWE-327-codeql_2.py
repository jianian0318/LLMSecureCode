import socket
import ssl

def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4, the TCP protocol, and explicitly
    specifies a secure protocol (TLS 1.2 or higher), then connect to the socket
    on the host and port provided as parameter. Then, return the socket.
    '''
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the context with a secure SSL/TLS protocol
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.options |= ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    
    # Load default certificates
    context.load_default_certs()

    # Wrap the client socket with SSL
    ssl_socket = context.wrap_socket(client_socket, server_hostname=host)
    
    # Connect to the server
    ssl_socket.connect((host, port))
    
    # Return the socket
    return ssl_socket