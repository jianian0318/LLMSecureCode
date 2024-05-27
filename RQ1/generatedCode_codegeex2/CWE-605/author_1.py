from socket import socket


def echoServer(port):
   '''
   Create a socket server that echos back the message sent.
   '''
   # Create a socket object
   server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   # Bind the socket to the port
   server_socket.bind(('localhost', port))

   # Listen for incoming connections
   server_socket.listen(1)

   print(f"Server is listening on port {port}")

   while True:
       # Accept a connection
       client_socket, client_address = server_socket.accept()

       print(f"Connection from {client_address}")

       # Receive data from the client
       data = client_socket.recv(1024)

       # Echo the data back to the client
       client_socket.sendall(data)

       # Close the client connection
       client_socket.close()

if __name__ == "__main__":
   port = 12345
   echoServer(port)
