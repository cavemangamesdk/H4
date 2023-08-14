from dataclasses import dataclass
from DataClass.DeviceDataBase import DeviceDataBase

@dataclass
class DeviceAccelerometerDataBase():
    # from get_accelerometer()
    roll: float
    pitch: float
    yaw: float
    # from get_accelerometer_raw()
    x_raw: float
    y_raw: float
    z_raw: float

@dataclass
class DeviceAccelerometerData(DeviceDataBase):
    data: DeviceAccelerometerDataBase