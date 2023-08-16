import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        #await websocket.send(message)
        print(f"Received: {message}")

start_server = websockets.serve(echo, "192.168.109.110", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
