import socket
import struct
import time

message = 'very important data'
multicast_group = ('224.1.1.1', 58008)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout to avoid blocking indefinitely
sock.settimeout(0.2)

# Set the time-to-live for messages to 1
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Send data to the multicast group
for i in range(1, 10):
    print(f'sending {i} "%s"' % message)
    sent = sock.sendto(message.encode(), multicast_group)
    time.sleep(1)

# Close the socket
sock.close()
