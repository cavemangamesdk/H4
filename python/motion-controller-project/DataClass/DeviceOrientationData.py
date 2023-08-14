from dataclasses import dataclass
from DataClass.DeviceDataBase import DeviceDataBase

@dataclass
class DeviceOrientationDataBase():
    # from get_orientation_degrees()
    roll_deg: float
    pitch_deg: float
    yaw_deg: float
    # from get_orientation_radians()
    roll_rad: float
    pitch_rad: float
    yaw_rad: float

@dataclass
class DeviceOrientationData(DeviceDataBase, DeviceOrientationDataBase):
    pass