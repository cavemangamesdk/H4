# Absolute Orientation (Quaterion). Four point quaternion output for more accurate data manipulation.

from dataclasses import dataclass

@dataclass
class Quaternion():
    x: float
    y: float
    z: float
    w: float