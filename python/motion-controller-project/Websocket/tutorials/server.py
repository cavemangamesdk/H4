#!/usr/bin/env python

import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with serve(echo, "192.168.109.110", 8764):
        await asyncio.Future()  # run forever

asyncio.run(main())