# Angular Velocity Vector. Three axis of 'rotation speed' in rad/s

from dataclasses import dataclass

@dataclass
class Gyroscope():
    # from get_gyroscope_raw()
    x: float
    y: float
    z: float