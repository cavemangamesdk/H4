import socket

group = '224.1.1.1'
port = 5004
ttl = 2

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Set the outgoing interface to wlan0
sock.setsockopt(socket.SOL_SOCKET, 25, b'wlan0\x00')

sock.sendto(b"hello world", (group, port))
