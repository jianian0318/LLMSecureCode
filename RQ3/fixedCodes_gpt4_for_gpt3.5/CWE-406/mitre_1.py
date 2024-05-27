import socket
import time

# Maximum messages per second
MAX_MESSAGES = 1000

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

    # Create time counter
    start_time = time.time()

    # Create message counter
    message_counter = 0

    # Listen for incoming DNS requests
    while True:
        if message_counter <= MAX_MESSAGES:
            data, addr = sock.recvfrom(1024)
            parseUDPpacket(data)
            resolved_name = resolveName(data)
            sendResponse(addr[0], resolved_name)
            message_counter += 1
        if time.time() - start_time > 1:
            message_counter = 0
            start_time = time.time()