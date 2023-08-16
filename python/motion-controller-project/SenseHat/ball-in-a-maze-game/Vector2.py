import math

class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    # Operator overloaders
    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __div__(self, other: float):
        return Vector2(self.x / other.x, self.y / other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self
    
    def __idiv__(self, other: float):
        self.x /= other.x
        self.y /= other.y
        return self
    
    # Extension methods
    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def magnitudeSquared(self):
        return self.x * self.x + self.y * self.y

    def dot(self, other):
        return self.x * other.x + self.y * other.y
 
    def dot(self, other: float):
        return Vector2(self.x * other, self.y * other)
    
    def perpDot(self, other):
        return self.x * other.y - self.y * other.x
    
    def perpDot(self, other: float):
        return Vector2(self.x * other.y, -self.y * other.x)
    
    def normalized(self):
        mag = self.magnitude()
        if mag != 0:
            self /= mag
    
