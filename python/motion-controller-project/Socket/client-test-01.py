import socket

HOST = '192.168.1.100'  # Replace with the IP address of your C# server
PORT = 12345  # Replace with the port number used in the C# server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Connected to C# server')

    message = 'Hello from Python client!'
    s.sendall(message.encode())

    data = s.recv(1024)
    response = data.decode()
    print('Received:', response)
