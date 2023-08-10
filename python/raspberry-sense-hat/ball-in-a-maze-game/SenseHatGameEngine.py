
from enum import Enum

class Led:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class LedMatrix:
    def __init___(self):
        self.leds = [[0 for i in range(8)] for j in range(8)]
    
    def set_pixel(self, x, y, r, g, b):
        self.leds[x][y] = Led(r, g, b)
    
    def get_pixel(self, x, y):
        return self.leds[x][y]
    
    def clear(self, r, g, b):
        for i in range(8):
            for j in range(8):
                self.set_pixel(i, j, r, g, b)
    
    
    

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