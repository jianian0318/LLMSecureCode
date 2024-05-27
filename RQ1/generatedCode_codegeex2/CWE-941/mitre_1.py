import socket

def parseUDPpacket(data):
    '''
    This function takes the data received from UDP packet and parse it.
    It extracts the IP address and port number from the data.
    It then returns a tuple containing the IP address and port number.
    '''
    # Your code to parse the data and extract the IP address and port number

def sendResponse(ip, port, response):
    '''
    This function takes the IP address, port number and response data as arguments.
    It then creates a UDP socket and sends the response data to the requested IP address and port number.
    '''
    # Your code to create a UDP socket and send the response data

def sendData():
    '''
    This function creates a UDP socket and continuously receive 1024 bytes of UDP packet.
    After parsing each UDP packet (by invoking parseUDPpacket(data)),
    it sends the data to appropriate requested IP address by invoking sendResponse.
    '''
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a local address and port
    sock.bind(('localhost', 12345))

    while True:
        # Receive 1024 bytes of UDP packet
        data, addr = sock.recvfrom(1024)

        # Parse the UDP packet
        ip, port = parseUDPpacket(data)

        # Send the response to the requested IP address
        sendResponse(ip, port, "Response data")
