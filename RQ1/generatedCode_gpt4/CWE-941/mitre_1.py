import socket


def parseUDPpacket(data):
    '''
    This function is for parsing a UDP packet.
    Assume the data received is of the format: "IP_ADDRESS:PAYLOAD"
    Returns a tuple (IP_ADDRESS, PAYLOAD)
    This is just a skeleton of function, feel free to modify it according to your use-case.
    '''
    ip, payload = data.decode().split(":")
    return ip, payload


def sendResponse(ip, data, server_socket):
    '''
    This function sends back the requested data to the provided IP_ADDRESS.
    '''
    server_socket.sendto(data.encode(), (ip, 8080))


def sendData():
    '''
    This function creates a UDP socket and continuously receives 1024 bytes of UDP packet.
    After parsing each UDP packet (by invoking parseUDPpacket(data)),
    it sends the data to the appropriate requested IP address by invoking sendResponse.
    '''

    # Creating a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Binding the socket to a particular IP and port
    server_socket.bind(("localhost", 8080))

    while True:
        data, addr = server_socket.recvfrom(1024)
        ip, payload = parseUDPpacket(data)
        sendResponse(ip, payload, server_socket)