# Acceleration Vector. Three axis of acceleration (gravity + linear motion) in m/s^2

from dataclasses import dataclass

@dataclass
class Acceleration():
    x: float
    y: float
    z: float