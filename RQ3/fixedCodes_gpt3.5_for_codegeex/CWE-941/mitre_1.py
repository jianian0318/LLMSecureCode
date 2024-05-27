import socket

def parseUDPpacket(data):
    ip = data[0]
    port = data[1]
    return (ip, port)

def sendResponse(ip, port, response):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(response.encode(), (ip, port))

def sendData():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', 12345))
    
    while True:
        data, addr = sock.recvfrom(1024)

        ip, port = parseUDPpacket(addr)

        sendResponse(ip, port, "Response data")