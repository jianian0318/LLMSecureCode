import socket
import time

REQUESTS_PER_SECOND_LIMIT = 10  # create a limit for requests per second
last_requests = []

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

def is_rate_limit_exceeded():
    global last_requests
    current_time = time.time()
    last_requests = [t for t in last_requests if current_time - t < 1]

    if len(last_requests) >= REQUESTS_PER_SECOND_LIMIT:
        return True

    last_requests.append(current_time)
    return False

def UDPMessaging(udp_ip, udp_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((udp_ip, udp_port))

    while True:
        if is_rate_limit_exceeded():
            print('Rate limit exceeded.')
            continue

        data, addr = sock.recvfrom(1024)
        dns_query = parseUDPpacket(data)
        IP_address = resolveName(dns_query)
        sendResponse(addr[0], IP_address)