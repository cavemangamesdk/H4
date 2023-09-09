import socket
import time

# Set up server
server_ip = '192.168.109.175'  # Change to your PC's IP address
orientation_data_port = 5100
joystick_data_port = 5101

orientation_data_address = (server_ip, orientation_data_port)
joystick_data_address = (server_ip, joystick_data_port)

# Create a UDP socket
orientation_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
joystick_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address
orientation_socket.bind(orientation_data_address)
joystick_socket.bind(joystick_data_address)

print(f"\nStarted UDP server at {orientation_data_address}\nWaiting for packet...")
print(f"\nStarted UDP server at {joystick_data_address}\nWaiting for packet...")

# Loop indefinitely to receive packets
while True:
    orientation_payload, orientation_client_address = orientation_socket.recvfrom(1024)  # Buffer size is 1024 bytes
    joystick_payload, joystick_client_address = joystick_socket.recvfrom(1024)  # Buffer size is 1024 bytes
    # print(f"Received packet from {orientation_client_address}: {orientation_payload}\n")
    # print(f"Received packet from {joystick_client_address}: {joystick_payload}\n")
    print(f"{orientation_payload} {joystick_payload}")
    #time.sleep(0.01)
