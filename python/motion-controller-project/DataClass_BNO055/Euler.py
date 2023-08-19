# Absolute Orientation (Euler Vector). Three axis orientation data based on a 360° sphere

from dataclasses import dataclass
from DataClass.DeviceDataBase import DeviceDataBase

@dataclass
class Euler():
    # from get_orientation_degrees()
    x: float
    y: float
    z: float