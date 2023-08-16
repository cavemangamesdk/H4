import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://192.168.109.110:8764") as websocket:
        await websocket.send("Hello world!")
        message = await websocket.recv()
        print(f"Received: {message}")

asyncio.run(hello())
