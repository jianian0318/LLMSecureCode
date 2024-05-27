import socket
import ssl

def connect(host, port):
    # Create a socket, specifying the IPv4 address family and TCP protocol
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Create a SSL Context with the recommended setting for a client-side socket
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT) # Use the highest version of TLS available    
    
    # Set the minimum version to TLSv1.2
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    
    # Require server certificate verification
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_default_certs() # Load default CA certificates
    
    # Wrap the socket with SSL
    ssl_sock = context.wrap_socket(sock, server_hostname=host)

    # Connect the SSL wrapped socket to the provided host and port
    ssl_sock.connect((host, port))
    
    # Return the connected SSL socket
    return ssl_sock

# Usage example
if __name__ == "__main__":
    host, port = 'www.example.com', 443
    ssl_socket = connect(host, port)
    
    # Remember to close the socket when done
    ssl_socket.close()