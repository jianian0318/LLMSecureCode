import socket
import ssl

def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4, specifies TLS version, and
    connects to the socket on the host and port provided as parameters.
    Then, return the socket.
    '''
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Create an SSL context with specific TLS version and use SSLv23
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)  # Fixed TLS version

    # Set options for insecure SSL/TLS versions
    context.options |= ssl.OP_NO_SSLv2
    context.options |= ssl.OP_NO_SSLv3
  
    # Wrap the socket with the SSL context
    ssl_sock = context.wrap_socket(sock, server_hostname=host)

    # Connect to the host and port
    server_address = (host, port)
    ssl_sock.connect(server_address)

    return ssl_sock