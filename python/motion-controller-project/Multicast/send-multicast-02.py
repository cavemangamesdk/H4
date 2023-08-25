import socket

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 58008

def send_multicast_message(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the interface
    if hasattr(socket, 'SO_BINDTODEVICE'):
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, b'wlan0')

    sock.sendto(message.encode(), (MCAST_GRP, MCAST_PORT))
    sock.close()

message = "Hello, multicast!"
send_multicast_message(message)
