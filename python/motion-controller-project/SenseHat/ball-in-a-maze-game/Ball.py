import math
from Vector2 import Vector2

class Ball:
    def __init__(self, pos: Vector2, vel: Vector2, mass: float, radius: float):
        self.pos = pos
        self.vel = vel
        self.frc = Vector2(0, 0)
        self.mass = mass
        self.radius = radius

    pos: Vector2
    vel: Vector2
    frc: Vector2
    mass: float
    radius: float