import asyncio
import websockets
import get_data as getData
from sense_hat import SenseHat
import json

sense = SenseHat()

async def get_data() -> str:
    return getData.getPitchRollData(sense)

async def echo(websocket, path):
    while True:
        await websocket.send(getData.getPitchRollData(sense))

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
