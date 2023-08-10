from sense_hat import SenseHat
from dataclasses import dataclass
import datetime
import uuid

@dataclass
class DeviceGyroData:
    sessionId: uuid
    timeStamp: datetime
    # from get_gyroscope()
    roll: float
    pitch: float
    yaw: float
    # from get_gyroscope_raw()
    x: float
    y: float
    z: float

def getData():
    
    sense = SenseHat()
    gyro = sense.get_gyroscope()
    gyroRaw = sense.get_gyroscope_raw()

    data = DeviceGyroData(
        sessionId = str(uuid.uuid4()),
        timeStamp = str(datetime.datetime.now()),
        roll = gyro['roll'],
        pitch = gyro['pitch'],
        yaw = gyro['yaw'],
        x = gyroRaw['x'],
        y = gyroRaw['y'],
        z = gyroRaw['z']
    )

    return data
