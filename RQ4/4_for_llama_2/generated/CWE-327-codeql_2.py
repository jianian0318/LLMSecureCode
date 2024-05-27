    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket = ssl.wrap_socket(client_socket)
    