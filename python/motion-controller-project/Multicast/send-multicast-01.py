import socket
import struct

MULTICAST_GROUP = '239.1.1.1'
MULTICAST_PORT = 8266

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sock.bind(('', MULTICAST_PORT))

# mreq = struct.pack("4sl", socket.inet_aton(MULTICAST_GROUP), socket.INADDR_ANY)
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# while True:
#     print(sock.recv(10240))


import time
import socket
import struct

MCAST_GRP = '239.1.1.1'  # replace with your multicast group IP
MCAST_PORT = 8266  # replace with your port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

while True:
    sock.sendto(b"Hello, World!", (MCAST_GRP, MCAST_PORT))
    time.sleep(1)


# import socket
# import time

# MCAST_GRP = '224.1.1.1'
# MCAST_PORT = 58008
# message = "robot"
# # regarding socket.IP_MULTICAST_TTL
# # ---------------------------------
# # for all packets sent, after two hops on the network the packet will not 
# # be re-sent/broadcast (see https://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
# MULTICAST_TTL = 2

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

# # For Python 3, change next line to 'sock.sendto(b"robot", ...' to avoid the
# # "bytes-like object is required" msg (https://stackoverflow.com/a/42612820)

# while True:
#     sock.sendto(message.encode(), (MCAST_GRP, MCAST_PORT))
#     print("sent")
#     time.sleep(1)