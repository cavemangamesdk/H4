import socket

# Set up server
server_ip = '192.168.109.1'  # Change to your PC's IP address
server_port = 5100  # Match this with the UDP port in your ESP8266 code
server_address = (server_ip, server_port)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
# Bind the socket to the server address
sock.bind(server_address)

print(f"\nStarted UDP server at {server_address}\nWaiting for packet...")

# Loop indefinitely to receive packets
while True:
    payload, client_address = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received packet from {client_address}: {payload}\n")
