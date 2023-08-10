from sense_hat import SenseHat
from dataclasses import dataclass
import datetime
import uuid

@dataclass
class DeviceAccelerometerData:
    sessionId: uuid
    timeStamp: datetime
    # from get_accelerometer()
    roll: float
    pitch: float
    yaw: float
    # from get_accelerometer_raw()
    x_raw: float
    y_raw: float
    z_raw: float

def getData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime):
        
    accel = senseHat.get_accelerometer()
    accelRaw = senseHat.get_accelerometer_raw()

    data = DeviceAccelerometerData(
        sessionId = str(sessionId),
        timeStamp = str(datetime.datetime.now()),
        roll = accel['roll'],
        pitch = accel['pitch'],
        yaw = accel['yaw'],
        x_raw = accelRaw['x'],
        y_raw = accelRaw['y'],
        z_raw = accelRaw['z']
    )

    return data