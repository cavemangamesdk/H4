from dataclasses import dataclass
from DataClass.DeviceData import DeviceData

@dataclass
class DeviceGyroscopeData(DeviceData):
    # from get_gyroscope()
    roll: float
    pitch: float
    yaw: float
    # from get_gyroscope_raw()
    x_raw: float
    y_raw: float
    z_raw: float
