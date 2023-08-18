import asyncio
import websockets

async def get_data():
    # This is where you would put your logic to get the data
    # For now, I'll just return a string
    return "This is the data to be sent to the client."

async def echo(websocket, path):
    while True:
        data = await get_data()
        await websocket.send(data)
        await asyncio.sleep(0.1)  # sleep for 0.1 seconds

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
