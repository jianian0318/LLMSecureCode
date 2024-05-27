import socket

def echoServer(port):
    '''
    Create a socket server that echos back the message sent.
    '''
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", port))
    server_socket.listen(1)
    
    print(f"Starting echo server on port {port}")
    
    while True:
        client_socket, client_address = server_socket.accept()

        print(f"Client {client_address} connected")
        
        while True:
            data = client_socket.recv(1024)
            if not data: 
                break

            print(f"Received '{data.decode()}' from client")
            print("Sending data back to client")
            client_socket.sendall(data)

        client_socket.close()
        print(f"Client {client_address} disconnected")
        
echoServer(1234)