import socket
hostname = "www.google.com"
addr_info = socket.getaddrinfo(hostname, 80)
for info in addr_info:
    print("IP Address:", info[4][0])