
from enum import Enum

class Led:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class LedMatrix:
    def __init___(self, width, height):
        self.leds = [[0 for i in range(width)] for j in range(height)]

class Joystick:
    pass

class Game:
    pass

class JoystickState(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    MIDDLE = 5