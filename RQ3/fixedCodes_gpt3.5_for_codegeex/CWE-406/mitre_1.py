import socket

def parseUDPpacket(data):
    dns_query = data.decode('utf-8').split(' ')[0]
    return dns_query

def resolveName(nameToResolve):
    try:
        IP_address = socket.gethostbyname(nameToResolve)
    except socket.gaierror:
        IP_address = "Unknown"
    return IP_address

def sendResponse(requestIP, record):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(str(record).encode('utf-8'), (requestIP, 123))
    sock.close()

def UDPMessaging(udp_ip, udp_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((udp_ip, udp_port))
    while True:
        data, addr = sock.recvfrom(1024)
        dns_query = parseUDPpacket(data)
        IP_address = resolveName(dns_query)
        sendResponse(addr[0], IP_address)