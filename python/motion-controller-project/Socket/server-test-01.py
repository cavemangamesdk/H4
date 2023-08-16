import socket

HOST = '192.168.109.175'  # Replace with the IP address of your Python server
PORT = 12345  # Replace with the port number you want to use

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    print(f"Client connected from {addr}")

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"Received: {message}")

            response = "Hello from Python server!"
            conn.sendall(response.encode())
            print(f"Sent: {response}")
