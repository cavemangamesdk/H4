from dataclasses import dataclass
from DataClass.DeviceDataBase import DeviceDataBase

@dataclass
class DeviceGyroscopeDataBase():
    # from get_gyroscope()
    roll: float
    pitch: float
    yaw: float
    # from get_gyroscope_raw()
    x_raw: float
    y_raw: float
    z_raw: float

@dataclass
class DeviceGyroscopeData(DeviceDataBase):
    data: DeviceGyroscopeDataBase.__dict__
