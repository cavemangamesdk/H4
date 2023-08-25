import asyncio
import websockets
import get_data_BNO055 as getData
import board # pip3 install adafruit-blinka
import adafruit_bno055 # pip3 install adafruit-circuitpython-bno055 (NOT adafruit-bno055)


i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c, address=0x29)

async def connect_and_run():
    async with websockets.connect("ws://192.168.109.1:8765/Tester") as websocket:
        #await get_data(websocket)
        while True:
            await websocket.send(getData.getPitchRollData(sensor))

asyncio.run(connect_and_run())
