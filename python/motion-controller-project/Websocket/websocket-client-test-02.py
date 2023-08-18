import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            message = await websocket.recv()
            print(f"Received: {message}")

asyncio.run(hello())
