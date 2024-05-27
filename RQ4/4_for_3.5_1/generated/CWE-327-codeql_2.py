import socket
import ssl

def connect(host, port):
    # Setup an SSL context to specify the use of TLS
    context = ssl.SSLContext(ssl.PROTOCOL_TLS) # For Python version prior to 3.6
    #context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT) # For Python version 3.6 and later
    context.options |= ssl.OP_NO_SSLv2
    context.options |= ssl.OP_NO_SSLv3
    context.options |= ssl.OP_NO_TLSv1
    context.options |= ssl.OP_NO_TLSv1_1
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_default_certs()

    # Create a client socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap socket with SSL support
    ssl_sock = context.wrap_socket(sock, server_hostname=host)

    # Connect to the socket on the host and port
    ssl_sock.connect((host, port))

    # Return the socket
    return ssl_sock