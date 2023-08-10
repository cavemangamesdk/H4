from dataclasses import dataclass
import datetime
import uuid

@dataclass
class DeviceCompassData:
    sessionId: uuid
    timeStamp: datetime
    # from get_compass()
    direction: float
    # from get_compass_raw()
    x: float
    y: float
    z: float