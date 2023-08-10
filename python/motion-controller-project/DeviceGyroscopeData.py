from sense_hat import SenseHat
from dataclasses import dataclass
import datetime
import uuid

@dataclass
class DeviceGyroscopeData:
    sessionId: uuid
    timeStamp: datetime
    # from get_gyroscope()
    roll: float
    pitch: float
    yaw: float
    # from get_gyroscope_raw()
    x_raw: float
    y_raw: float
    z_raw: float

def getData(senseHat: SenseHat, uuid: uuid.UUID):
    
    gyro = senseHat.get_gyroscope()
    gyroRaw = senseHat.get_gyroscope_raw()

    data = DeviceGyroscopeData(
        sessionId = str(uuid),
        timeStamp = str(datetime.datetime.now()),
        roll = gyro['roll'],
        pitch = gyro['pitch'],
        yaw = gyro['yaw'],
        x_raw = gyroRaw['x'],
        y_raw = gyroRaw['y'],
        z_raw = gyroRaw['z']
    )

    return data
