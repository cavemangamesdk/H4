import asyncio
import websockets
import get_data_BNO055 as getData
import board # pip3 install adafruit-blinka
import adafruit_bno055 # pip3 install adafruit-circuitpython-bno055 (NOT adafruit-bno055)
import socket
import requests
import time
import netifaces as ni
import asyncio
import psutil

# To-do:
# - Replace get_ip_address() with function that gets the local IP address of the device without needing internet connection
# - close all websockets on program stop


i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c, address=0x29)

def get_local_ip_address(interface) -> str:
    interface_addrs = psutil.net_if_addrs().get(interface) or []
    for snicaddr in interface_addrs:
            if snicaddr.family == socket.AF_INET:
                    return snicaddr.address
    return False

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

while not get_local_ip_address("wlan0"):
    print("Waiting for internet connection...")
    time.sleep(1)

start_server = websockets.serve(echo, get_local_ip_address("wlan0"), 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
