# Magnetic Field Strength Vector. Three axis of magnetic field sensing in micro Tesla (uT).

from dataclasses import dataclass

@dataclass
class Magnetometer():
    x: float
    y: float
    z: float