import asyncio
import websockets
import get_data as getData
from sense_hat import SenseHat
import threading, time, keyboard, datetime, json, uuid

sense = SenseHat()
uuidDevice = uuid.uuid4()
dateTime = datetime

async def echo(websocket, path):
    data = getData.getPitchRollData(sense, uuidDevice, dateTime)
    # send data over websocket 
    async for message in websocket:
        await websocket.send(data)
        print(f"Received: {message}")



start_server = websockets.serve(echo, "192.168.109.110", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
