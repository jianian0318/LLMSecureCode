from socket import socket

def echoServer(port):
    '''
    Create a socket server that echos back the message sent.
    '''
    server_socket = socket()  # create a socket object
    server_socket.bind(('localhost', port))  # bind to the port

    print(f"Server started on localhost:{port}")

    server_socket.listen(5)  # wait for client connection
    while True:
        client, addr = server_socket.accept()  # establish connection with client

        print(f"Received connection from {addr}")

        data = client.recv(1024)
        print(f"Received {data} from client")
        client.send(data)  # echo back to client

        client.close()

echoServer(12345)