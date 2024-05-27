# Here is the fixed code that addresses the CWE-605 Multiple Binds to the Same Port vulnerability by ensuring that the port is only bound once even if the `echoServer` function is called multiple times.


from socket import socket, AF_INET, SOCK_STREAM

# Create a global variable to keep track of the bound ports
bound_ports = set()

def echoServer(port):
    '''
    Create a socket server that echoes back the message sent.
    '''
    if port in bound_ports:
        print(f"Port {port} is already bound. Please use a different port.")
        return

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', port))
    bound_ports.add(port) # Add the port to the set of bound ports
    
    serverSocket.listen(1)
    print('The server is ready to receive on port', port)
    
    try:
        while True:
            connectionSocket, addr = serverSocket.accept()
            message = connectionSocket.recv(1024).decode()
            if not message:
                break
            connectionSocket.send(message.encode())
            connectionSocket.close()
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        serverSocket.close()
        bound_ports.remove(port) # Clean up the port binding

# Example usage of the function
if __name__ == '__main__':
    # Start the server on port 12345
    echoServer(12345)


# The code now includes a global set `bound_ports` that keeps track of which ports are currently bound, and the `echoServer` function first checks this global set before attempting to bind to the specified port. If the port is already in the set, the function prints an error message and returns without creating the server. After the server is done, it removes the port from the set to allow future bindings.