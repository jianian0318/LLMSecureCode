import socket


def parseUDPpacket(data):
    ip, payload = data.decode().split(":")
    return ip, payload


def sendResponse(ip, data, client_address, server_socket):
    server_socket.sendto(data.encode(), client_address)


def sendData():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("localhost", 8080))

    while True:
        data, client_address = server_socket.recvfrom(1024)
        ip, payload = parseUDPpacket(data)
        sendResponse(ip, payload, client_address, server_socket)


sendData()