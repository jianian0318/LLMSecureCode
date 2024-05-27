import socket

def parseUDPpacket(data):
    # Parse the UDP packet and return the domain name to resolve
    domain_name = data.decode("utf-8")
    return domain_name


def resolveName(nameToResolve):
    # Resolve the domain name and return the IP address
    ip_address = socket.gethostbyname(nameToResolve)
    return ip_address


def sendResponse(requestIP, record):
    # Send the DNS record back to the requesting IP
    response = record.encode("utf-8")
    sock.sendto(response, requestIP)


def UDPMessaging(udp_ip, udp_port):
    '''
    Create a UDP socket that listens on the IP and port provided for DNS requests.
    Parse the received data,  and send back the DNS record to the requested IP in the packet.
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((udp_ip, udp_port))

    while True:
        data, addr = sock.recvfrom(1024)
        domain_name = parseUDPpacket(data)
        ip_address = resolveName(domain_name)
        sendResponse(addr, ip_address)