from dataclasses import dataclass
from DeviceData import DeviceData

@dataclass
class DeviceMagnetometerData(DeviceData):
    # from get_compass()
    north: float
    # from get_compass_raw()
    x_raw: float
    y_raw: float
    z_raw: float