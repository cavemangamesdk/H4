import socket
import time

def broadcast_ip_address():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Get the localhost IP address
    #ip_address = socket.gethostbyname(socket.gethostname())
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.connect(("8.8.8.8", 80))
    ip_address = my_socket.getsockname()[0]
    #print('Your IP Address is',my_socket.getsockname()[0])
    print(ip_address)
    my_socket.close()


    # Broadcast the IP address
    broadcast_address = '<broadcast>'
    message = ip_address.encode('utf-8')
    sock.sendto(message, (broadcast_address, 12345))

    # Close the socket
    sock.close()

# Call the function to broadcast the IP address
while True:
    broadcast_ip_address()
    time.sleep(1)