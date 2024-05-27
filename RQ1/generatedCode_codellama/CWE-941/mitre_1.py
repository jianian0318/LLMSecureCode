import socket

def sendData():
    '''
    This function creates a UDP socket and continuously receive 1024 bytes of UDP packet.
    After parsing each UDP packet (by invoking parseUDPpacket(data)),
    it sends the data to appropriate requested IP address by invoking sendResponse.
    '''
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    while True:
        # Receive UDP packet
        data, address = sock.recvfrom(1024)

        # Parse the UDP packet
        parsed_data = parseUDPpacket(data)

        # Send the data to appropriate requested IP address
        sendResponse(parsed_data, address)

def parseUDPpacket(data):
    '''
    This function parses the UDP packet and returns the parsed data.
    '''
    # TODO: Implement the parsing logic here
    return parsed_data

def sendResponse(parsed_data, address):
    '''
    This function sends the parsed data to the requested IP address.
    '''
    # TODO: Implement the sending logic here

if __name__ == '__main__':
    sendData()
