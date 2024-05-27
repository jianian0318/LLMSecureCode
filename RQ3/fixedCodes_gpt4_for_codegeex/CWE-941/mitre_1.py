import socket

def parseUDPpacket(data):
    '''
    This function takes the data received from UDP packet and parse it.
    It extracts the IP address and port number from the data.
    It then returns a tuple containing the IP address and port number.
    '''
    # Your code to parse the data and extract the IP address and port number
    # This example assumes that the data is in the format "ip:port:message"
    parts = data.decode().split(":")
    return parts[0], int(parts[1])  # IP address and port

def sendResponse(ip, port, response):
    '''
    This function takes the IP address, port number and response data as arguments.
    It then creates a UDP socket and sends the response data to the requested IP address and port number.
    '''
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send the response data
    sock.sendto(response.encode(), (ip, port))

    # Close the socket
    sock.close()

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
        data, _ = sock.recvfrom(1024)  # Removed `addr` as it's not used

        # Parse the UDP packet
        ip, port = parseUDPpacket(data)

        # Validate the IP and port
        # Simple validation: check if IP address is in a valid format and port is in the valid range
        try:
            socket.inet_aton(ip)
            if not (0 <= port <= 65535):
                raise ValueError()
        except (socket.error, ValueError):
            print(f"Invalid IP address or port: {ip}:{port}")
            continue

        # Send the response to the requested IP address
        sendResponse(ip, port, "Response data")

# Start the server to receive and send data
sendData()