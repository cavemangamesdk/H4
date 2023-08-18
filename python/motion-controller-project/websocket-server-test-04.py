import asyncio
import websockets
import get_data as getData
from sense_hat import SenseHat
import json
import socket
import time
import netifaces

sense = SenseHat()

broadcasting = True

def get_ip_address() -> str:
    # Get the localhost IP address
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.connect(("8.8.8.8", 80))
    ip_address = socket.getsockname()[0]
    socket.close()
    
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
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Get the localhost IP address
    ip_address = get_ip_address()
    print(ip_address)

    # Broadcast the IP address
    broadcast_address = get_broadcast_address(ip_address)
    print(broadcast_address)
    message = ip_address.encode('utf-8')

    socket.sendto(message, (broadcast_address, 12345))
    print(f"broadcast message: {message}")
    
    # Close the socket
    socket.close()

async def send_data(websocket, path):
    
    global broadcasting
    print("Client connected")
    broadcasting = False

    while True:
        await websocket.send(getData.getPitchRollData(sense))

start_server = websockets.serve(send_data, "localhost", 8765)

while broadcasting:
    broadcast_ip_address()
    time.sleep(1)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
