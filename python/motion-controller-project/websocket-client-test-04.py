import asyncio
import websockets
import time

async def get_data(websocket):
    while True:
        message = await websocket.recv()
        print(message)

async def connect_and_run(websocket):
    n = 0
    while True:
        await websocket.send(f"Hej Pierre!!! {n}")
        n = n+1
        await asyncio.sleep(1)

async def main():
    async with websockets.connect("ws://192.168.109.1:8765/Tester") as websocket:
        task1 = asyncio.create_task(get_data(websocket))
        task2 = asyncio.create_task(connect_and_run(websocket))
        await asyncio.gather(task1, task2)

asyncio.run(main())
