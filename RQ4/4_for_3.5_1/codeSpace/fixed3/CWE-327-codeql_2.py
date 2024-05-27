import socket
import ssl

def connect(host, port):
    # Setup an SSL context to specify the use of TLS
    # Note: ssl.PROTOCOL_TLS_CLIENT will choose the highest protocol version that both the client and server support.
    # On older versions (prior to Python 3.6), you should use ssl.PROTOCOL_TLS or ssl.PROTOCOL_TLSv1_2 to specify TLS 1.2
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
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