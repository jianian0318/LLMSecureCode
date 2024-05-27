import socket

def parseUDPpacket(data):
    '''
    Implement your own parser here
    '''
    ip = '' # Fetch IP from data
    message = '' # Fetch message from data
    return ip, message

def sendResponse(soc, ip, data):
    '''
    Function to send the response to the requested IP
    '''
    soc.sendto(data, (ip, 5000)) # Sending the data, assuming the destination port is 5000

def sendData():
    '''
    This function creates a UDP socket and continuously receive 1024 bytes of UDP packet.
    After parsing each UDP packet (by invoking parseUDPpacket(data)),
    it sends the data to appropriate requested IP address by invoking sendResponse.
    '''
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind(("localhost", 12345)) # Assuming "localhost" as the host, using port 12345. Modify as per requirements

    while True:
        data, addr = UDPServerSocket.recvfrom(1024)
        ip, message = parseUDPpacket(data)
        sendResponse(UDPServerSocket, ip, message)