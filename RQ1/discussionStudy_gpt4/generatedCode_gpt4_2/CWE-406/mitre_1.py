import socket

def parseUDPpacket(data):
    # Add code here to parse the UDP packet
    pass

def resolveName(nameToResolve):
    # Add code here to resolve the DNS name
    pass

def sendResponse(requestIP, record):
    # Add code here to send DNS record back to the requester
    pass

def UDPMessaging(udp_ip, udp_port):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the provided IP and port
    sock.bind((udp_ip, udp_port))

    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        nameToResolve = parseUDPpacket(data)
        record = resolveName(nameToResolve)
        sendResponse(addr[0], record)