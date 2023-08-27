import socket

MCAST_GRP = '239.1.1.1'
MCAST_PORT = 8266

hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)  
print(IPAddr)

def receive_multicast_message():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the IP address of wlan0
    sock.bind((IPAddr, MCAST_PORT))  # Replace with the actual IP address of wlan0

    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MCAST_GRP) + socket.inet_aton('0.0.0.0'))

    while True:
        data, addr = sock.recvfrom(1024)
        print("Received message:", data.decode())

receive_multicast_message()
