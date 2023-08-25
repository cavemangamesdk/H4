import socket

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 58008

def receive_multicast_message():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the interface
    if hasattr(socket, 'SO_BINDTODEVICE'):
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, b'wlan0')

    sock.bind((MCAST_GRP, MCAST_PORT))
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MCAST_GRP) + socket.inet_aton('0.0.0.0'))

    while True:
        data, addr = sock.recvfrom(1024)
        print("Received message:", data.decode())

receive_multicast_message()
