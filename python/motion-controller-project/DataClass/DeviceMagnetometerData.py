from dataclasses import dataclass
from DataClass.DeviceDataBase import DeviceDataBase

@dataclass
class DeviceMagnetometerDataBase():
    # from get_compass()
    north: float
    # from get_compass_raw()
    x_raw: float
    y_raw: float
    z_raw: float

@dataclass
class DeviceMagnetometerData(DeviceDataBase):
    data: DeviceMagnetometerDataBase