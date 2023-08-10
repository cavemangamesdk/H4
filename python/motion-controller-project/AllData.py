from sense_hat import SenseHat
from dataclasses import dataclass
import datetime
import uuid

import DeviceAccellerometerData

# get all sense hat data
@dataclass
class SenseHatData:
    sessionId: uuid
    timeStamp: datetime
    # from get_accelerometer()
    roll: float
    pitch: float
    yaw: float
    # from get_accelerometer_raw()
    x: float
    y: float
    z: float
    # from get_gyroscope()
    roll: float
    pitch: float
    yaw: float
    # from get_gyroscope_raw()
    x: float
    y: float
    z: float
    # from get_temperature()
    temperature: float
    # from get_humidity()
    humidity: float
    # from get_pressure()
    pressure: float

