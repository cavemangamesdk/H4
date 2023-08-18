import asyncio
import websockets
import get_data as getData
from sense_hat import SenseHat
import json
import socket

sense = SenseHat()

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

start_server = websockets.serve(echo, get_ip_address(), 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
