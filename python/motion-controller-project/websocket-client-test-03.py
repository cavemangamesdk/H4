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
import time

async def get_data(websocket):
    while True:
        message = await websocket.recv()
        print(message)

async def connect_and_run():
    n = 0
    async with websockets.connect("ws://192.168.109.1:8765/Tester") as websocket:
        #await get_data(websocket)
        while True:
            await websocket.send(f"Hej Pierre!!! {n}")
            n = n+1
            time.sleep(1)

connect_and_run()

#asyncio.run(connect_and_run)
# asyncio.get_event_loop().run_until_complete(connect_and_run)
# asyncio.Future()

