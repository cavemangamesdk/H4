# Gravity Vector. Three axis of gravitational acceleration (minus movement) in m/s^2

from dataclasses import dataclass

@dataclass
class Gravity():
    x: float
    y: float
    z: float