# Linear Acceleration Vector. Three axis of linear acceleration data (acceleration minus gravity) in m/s^2

from dataclasses import dataclass

@dataclass
class LinearAcceleration():
    x: float
    y: float
    z: float