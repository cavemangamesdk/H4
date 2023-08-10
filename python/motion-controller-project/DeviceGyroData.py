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