import socket

def parseUDPpacket(data):
    # Add code to parse UDP packet if needed
    pass

def resolveName(nameToResolve):
    # Add code to resolve name if needed
    pass


def sendResponse(requestIP, record):
    # Add code to send response if needed
    pass
  

def UDPMessaging(udp_ip, udp_port):
    '''
    Create a UDP socket that listens on the IP and port provided for DNS requests.
    Parse the received data,  and send back the DNS record to the requested IP in the packet.
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((udp_ip, udp_port))
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        record = parseUDPpacket(data)
        requestIP = resolveName(record)
        sendResponse(requestIP, record)