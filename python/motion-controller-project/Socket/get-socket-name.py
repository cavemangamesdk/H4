import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("8.8.8.8", 80))
local_ip = sock.getsockname()[0]

print(local_ip)
