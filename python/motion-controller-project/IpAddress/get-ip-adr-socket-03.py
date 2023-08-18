import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.connect(("8.8.8.8", 80))
print('Your IP Address is',my_socket.getsockname()[0])