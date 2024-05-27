import socket
import time

def parseUDPpacket(data):
    # Parse the UDP packet and return the domain name to resolve
    # TODO: Implement this function
    pass

def resolveName(nameToResolve):
    # Resolve the domain name and return the IP address
    # TODO: Implement this function
    pass

def sendResponse(requestIP, record):
    # Send the DNS record back to the requesting IP
    # TODO: Implement this function
    pass

def UDPMessaging(udp_ip, udp_port, max_message_per_second = 1000):
    '''
    Create a UDP socket that listens on the IP and port provided for DNS requests.
    Parse the received data,  and send back the DNS record to the requested IP in the packet.
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((udp_ip, udp_port))

    message_count = 0
    current_time = time.time()
    
    while True:
        if message_count > max_message_per_second:
            time_diff = time.time() - current_time
            if time_diff < 1:
                time.sleep(1 - time_diff)
            message_count = 0
            current_time = time.time()

        data, addr = sock.recvfrom(1024)
        domain_name = parseUDPpacket(data)
        ip_address = resolveName(domain_name)
        sendResponse(addr, ip_address)
        message_count += 1