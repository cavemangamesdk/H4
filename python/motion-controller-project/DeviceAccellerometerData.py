from dataclasses import dataclass
import datetime
import uuid

@dataclass
class DeviceAccellerometerData:
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