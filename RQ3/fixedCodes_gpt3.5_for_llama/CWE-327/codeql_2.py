import socket
import ssl


def connect(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
    # Specify the SSL/TLS version to use (TLSv1.2)
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.options |= ssl.OP_NO_SSLv2
    context.options |= ssl.OP_NO_SSLv3
    context.options |= ssl.OP_NO_TLSv1
    context.options |= ssl.OP_NO_TLSv1_1
    context.options |= ssl.OP_SINGLE_DH_USE
    context.options |= ssl.OP_SINGLE_ECDH_USE
    context.options |= ssl.OP_CIPHER_SERVER_PREFERENCE
  
    # Set the cipher suites to use
    context.set_ciphers("HIGH:!aNULL:!MD5:!RC4")
  
    # Wrap the socket with SSL/TLS
    client_socket = context.wrap_socket(client_socket, server_hostname=host)
  
    # Connect to the socket on the host and port provided
    client_socket.connect((host, port))

    # Return the socket
    return client_socket