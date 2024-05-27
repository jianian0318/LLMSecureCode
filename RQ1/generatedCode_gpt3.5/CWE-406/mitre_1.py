import socket

def parseUDPpacket(data):
    pass


def resolveName(nameToResolve):
    pass


def sendResponse(requestIP, record):
    pass


def UDPMessaging(udp_ip, udp_port):
    '''
    Create a UDP socket that listens on the IP and port provided for DNS requests.
    Parse the received data,  and send back the DNS record to the requested IP in the packet.
    '''
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the IP and port provided
    sock.bind((udp_ip, udp_port))

    # Listen for incoming DNS requests
    while True:
        data, addr = sock.recvfrom(1024)
        parseUDPpacket(data)
        resolved_name = resolveName(data)
        sendResponse(addr[0], resolved_name)