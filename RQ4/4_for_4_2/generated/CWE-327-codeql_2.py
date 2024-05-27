import socket
import ssl

def connect(host, port):
    # Create a socket with IPV4 and TCP protocol
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the context with the specific TLS version
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    
    # Wrap the socket with SSL
    ssl_socket = context.wrap_socket(client_socket)
    
    # Connect to the given host and port
    ssl_socket.connect((host, port))

    # Return the SSL wrapped socket
    return ssl_socket


# Example use
# host = 'example.com'
# port = 443
# ssl_socket = connect(host, port)
# Remember to close the socket when you're done with ssl_socket.close()