# import asyncio
# import websockets

# async def hello():
#     async with websockets.connect("ws://192.168.109.110:8765") as websocket:
#         while True:
#             message = await websocket.recv()
#             print(message)

# asyncio.run(hello())

import asyncio
import websockets

async def get_data(websocket):
    while True:
        message = await websocket.recv()
        print(message)

async def connect_and_run():
    async with websockets.connect("ws://192.168.109.110:8765") as websocket:
        await get_data(websocket)

asyncio.run(connect_and_run())

