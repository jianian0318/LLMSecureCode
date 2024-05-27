import socket

def sendData():
    '''
    This function creates a UDP socket and continuously receives 1024 bytes of UDP packet.
    After parsing each UDP packet (by invoking parseUDPpacket(data)),
    it sends the data to the appropriate requested IP address by invoking sendResponse.
    '''

    def parseUDPpacket(data):
        '''
        This function parses the UDP packet and returns the parsed data.
        '''
        # Your code to parse the UDP packet goes here
        pass

    def sendResponse(data, ipAddress):
        '''
        This function sends the parsed data to the requested IP address.
        '''
        # Your code to send the response goes here
        pass

    while True:
        # Create a UDP socket
        udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Receive 1024 bytes of UDP packet
        data, address = udpSocket.recvfrom(1024)

        # Parse the UDP packet
        parsedData = parseUDPpacket(data)

        # Send the parsed data to the appropriate IP address
        sendResponse(parsedData, address[0])