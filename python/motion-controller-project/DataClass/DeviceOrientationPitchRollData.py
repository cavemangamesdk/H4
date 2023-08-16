from dataclasses import dataclass
from DataClass.DeviceDataBase import DeviceDataBase

# This class is for sending data to the Unity game engine.

@dataclass
class DeviceOrientationPitchRollData():
    # from get_orientation_degrees()
    roll: float
    pitch: float