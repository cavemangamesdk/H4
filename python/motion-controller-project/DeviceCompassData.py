from dataclasses import dataclass
import datetime

@dataclass
class DeviceCompassData:
    timeStamp: datetime
    # from get_compass()
    direction: float
    # from get_compass_raw()
    x: float
    y: float
    z: float