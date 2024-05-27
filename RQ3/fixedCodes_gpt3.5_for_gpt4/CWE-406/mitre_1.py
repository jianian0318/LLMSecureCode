import socket

def parseUDPpacket(data):
    return data

def resolveName(nameToResolve):
    return nameToResolve

def sendResponse(requestIP, record):
    pass

def UDPMessaging(udp_ip, udp_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((udp_ip, udp_port))

    while True:
        data, addr = sock.recvfrom(1024)
        packet = parseUDPpacket(data)
        record = resolveName(packet)
        sendResponse(addr[0], record)

UDPMessaging('127.0.0.1', 53)