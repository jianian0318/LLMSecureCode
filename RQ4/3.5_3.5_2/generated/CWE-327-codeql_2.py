def connect(host, port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the socket with SSL
    ssl_sock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLS)

    # Connect to the server
    ssl_sock.connect((host, port))

    return ssl_sock

# Example usage to connect to "example.com" on port 443
host = "example.com"
port = 443
ssl_socket = connect(host, port)
print("Connected to", host, "on port", port)