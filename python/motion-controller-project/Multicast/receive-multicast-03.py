import socket
import struct

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007
IS_ALL_GROUPS = True

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the wlan0 interface
sock.bind(('wlan0', MCAST_PORT))

if IS_ALL_GROUPS:
    # On this port, receives ALL multicast groups
    sock.bind(('', MCAST_PORT))
else:
    # On this port, listen ONLY to MCAST_GRP
    sock.bind((MCAST_GRP, MCAST_PORT))

mreq = struct.pack('4sl', socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    print(sock.recv(10240))
