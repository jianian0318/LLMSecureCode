import socket
import ssl

def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as parameter.
    Then, return the socket.
    '''
    # Create a regular socket using IPV4 (AF_INET) and TCP (SOCK_STREAM)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Wrap the socket with SSL support. Specifies SSL/TLS protocol version to use.
    # Using ssl.PROTOCOL_TLSv1_2 or ssl.PROTOCOL_TLSv1_3 (if available in your Python version) is recommended.
    ssl_socket = ssl.wrap_socket(client_socket, ssl_version=ssl.PROTOCOL_TLSv1_2)
    
    # Connect to the server on provided host and port
    ssl_socket.connect((host, port))
    
    # Return the SSL wrapped socket
    return ssl_socket

# Example usage
# Assuming there's a server running on localhost using port 443 (HTTPS default port)
host = 'www.example.com'
port = 443
secure_socket = connect(host, port)
print("Connected securely to", host, "on port", port)
secure_socket.close()