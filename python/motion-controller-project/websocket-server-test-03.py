import asyncio
import websockets
import get_data as getData
from sense_hat import SenseHat
import json

sense = SenseHat()

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

start_server = websockets.serve(echo, "192.168.109.89", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
