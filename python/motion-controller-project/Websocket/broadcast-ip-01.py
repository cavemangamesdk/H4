from time import sleep
from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST, gethostbyname, gethostname

PORT = 50000
MAGIC = "fna349fn"  # To ensure we don't confuse or get confused by other programs

s = socket(AF_INET, SOCK_DGRAM)  # Create UDP socket
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)  # This is a broadcast socket

my_ip = "192.168.24.175" #gethostbyname(gethostname())  # Get our IP. Be careful if you have multiple network interfaces or IPs
print(my_ip)

while True:
    data = MAGIC + my_ip
    s.sendto(data.encode(), ('<broadcast>', PORT))
    print("sent service announcement")
    sleep(5)
