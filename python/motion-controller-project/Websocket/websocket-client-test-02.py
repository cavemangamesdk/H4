import asyncio
import websockets

data = 'Message received: sensehat/imu/orientation 1 b{"session_id": "480cd0ac-2379-4fa4-a889-78b6cecc1835", "timestamp": "2023-08-16 09:08:34.122261", "data": {"roll_deg": 23.67335028589957, "pitch_deg": 6.138737957594272, "yaw_deg": 111.19384044240678, "roll_rad": 0.4131779074668884, "pitch_rad": 0.10714118182659149, "yaw_rad": 1.940916895866394}}'

async def hello():
    async with websockets.connect("ws://192.168.109.110:8765") as websocket:
        #await websocket.send("Hello world!")
        await websocket.send(data)
        message = await websocket.recv()
        print(f"Received: {message}")

asyncio.run(hello())
