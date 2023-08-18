import asyncio
import websockets
import get_data as getData
from sense_hat import SenseHat
import json
import socket
import requests
import time

sense = SenseHat()

def check_internet_connectivity() -> bool:
    try:
        requests.get('https://www.google.com', timeout=5)
        print("Internet connection available.")
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

def get_ip_address() -> str:

    # Get the localhost IP address
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.connect(("8.8.8.8", 80))
    ip_address = my_socket.getsockname()[0]
    print(f"ip address: {ip_address}")
    my_socket.close()
    
    return ip_address

async def get_data() -> str:
    # This is where you would put your logic to get the data
    # For now, I'll just return a string
    #return getData.getImuData(sense, uuidDevice, dateTime)
    return getData.getPitchRollData(sense)

async def echo(websocket, path):
    while True:
        # data = await get_data()
        # await websocket.send(data)
        await websocket.send(getData.getPitchRollData(sense))
        #await asyncio.sleep(0.1)  # sleep for 0.1 seconds

while not check_internet_connectivity():
    print("Waiting for internet connection...")
    time.sleep(1)

start_server = websockets.serve(echo, get_ip_address(), 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
