# Here is the fixed code:

from socket import *
import threading

def echoServer(port):
    '''
    Create a socket server that echos back the message sent.
    '''
    # Create a socket object
    server_socket = socket(AF_INET, SOCK_STREAM)

    # Configure the SO_REUSEADDR before you bind the socket to a specific address
    # This allows the server to start and stop without waiting for old connections to time out.
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # Bind the socket to the port
    try:
        server_socket.bind(('localhost', port))
    except socket.error as e:
        print(str(e))

    # Listen for incoming connections
    server_socket.listen(1)

    print(f"Server is listening on port {port}")

    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()

        print(f"Connection from {client_address}")

        # Create a separate thread for each incoming connection
        threading.Thread(target=client_thread, args=(client_socket,)).start()


def client_thread(connection):
    # Receive data from the client
    data = connection.recv(1024)
    
    # Echo the data back to the client
    connection.sendall(data)

    # Close the client connection
    connection.close()

if __name__ == "__main__":
    port = 12345
    echoServer(port)