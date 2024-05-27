import socket

def parseUDPpacket(data):
    '''
    Parse the UDP packet data and extract the DNS query.
    '''
    # Extract the DNS query from the data
    dns_query = data.decode('utf-8').split(' ')[0]

    return dns_query


def resolveName(nameToResolve):
    '''
    Resolve the domain name to an IP address using the socket library.
    '''
    try:
        IP_address = socket.gethostbyname(nameToResolve)
    except socket.gaierror:
        IP_address = "Unknown"

    return IP_address


def sendResponse(requestIP, record):
    '''
    Send the DNS record back to the requester.
    '''
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send the DNS record back to the requester
    sock.sendto(str(record).encode('utf-8'), (requestIP, 123))

    # Close the socket
    sock.close()


def UDPMessaging(udp_ip, udp_port):
    '''
    Create a UDP socket that listens on the IP and port provided for DNS requests.
    Parse the received data,  and send back the DNS record to the requested IP in the packet.
    '''
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the IP and port
    sock.bind((udp_ip, udp_port))

    while True:
        # Receive data from the client
        data, addr = sock.recvfrom(1024)

        # Parse the UDP packet
        dns_query = parseUDPpacket(data)

        # Resolve the domain name
        IP_address = resolveName(dns_query)

        # Send the DNS record back to the requester
        sendResponse(addr[0], IP_address)
