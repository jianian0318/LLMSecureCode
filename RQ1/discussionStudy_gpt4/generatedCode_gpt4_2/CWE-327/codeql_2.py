import socket
import ssl


def connect(host, port):
    '''
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as parameter.
    Then, return the socket.
    '''
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = ssl.wrap_socket(raw_socket)

    try:
        conn.connect((host, port))
    except socket.error as e:
        print(f"Failed to connect due to error: {e}")
        return None
    return conn