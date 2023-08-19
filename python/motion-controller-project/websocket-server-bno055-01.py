import asyncio
import websockets
import get_data_BNO055 as getData
import board # pip3 install adafruit-blinka
import adafruit_bno055 # pip3 install adafruit-circuitpython-bno055 (NOT adafruit-bno055)
import socket
import requests
import time

i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c, address=0x29)

def check_internet_connectivity() -> bool:
    try:
        requests.get('https://www.google.com', timeout=5)
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

async def echo(websocket, path):
    while True:
        # data = await get_data()
        # await websocket.send(data)
        try:
            data = getData.getPitchRollData(sensor)
        except:
            data = "0.0, 0.0, 0.0"
        try:
            await websocket.send(getData.getPitchRollData(sensor))
        except:
            pass

while not check_internet_connectivity():
    print("Waiting for internet connection...")
    time.sleep(1)

start_server = websockets.serve(echo, get_ip_address(), 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
