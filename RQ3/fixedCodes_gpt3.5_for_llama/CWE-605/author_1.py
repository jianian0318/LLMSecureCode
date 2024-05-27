from socket import socket

def echoServer(port):
    server_socket = socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)

    while True:
        connection, address = server_socket.accept()

        try:
            data = connection.recv(1024)
            connection.sendall(data)
        finally:
            connection.close()