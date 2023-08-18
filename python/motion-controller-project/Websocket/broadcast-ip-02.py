import socket
import time
import netifaces

def get_ip_address() -> str:
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Get the localhost IP address
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.connect(("8.8.8.8", 80))
    ip_address = my_socket.getsockname()[0]
    my_socket.close()
    
    return ip_address

def get_broadcast_address(ip_address) -> str:
    
    interfaces = netifaces.interfaces()

    # Find interface with ip_address
    for interface in interfaces:
        if netifaces.AF_INET in netifaces.ifaddresses(interface):
            for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                if link['addr'] == ip_address:
                    broadcast_address = link['broadcast']
                    break
    
    return broadcast_address

def broadcast_ip_address():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Get the localhost IP address
    ip_address = get_ip_address()
    print(ip_address)

    # Broadcast the IP address
    broadcast_address = get_broadcast_address(ip_address)
    print(broadcast_address)
    message = ip_address.encode('utf-8')
    sock.sendto(message, (broadcast_address, 12345))

    # Close the socket
    sock.close()

# Call the function to broadcast the IP address
while True:
    broadcast_ip_address()
    time.sleep(1)