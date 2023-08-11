from sense_hat import SenseHat
import math
import time

sense = SenseHat()

x = 1
y = 1

while True:

    x += 0.11
    y += 0.07

    x_screen = 1 + math.sin(x) * 6
    y_screen = 1 + math.cos(y) * 6

    sense.clear(0, 0, 0)

    sense.set_pixel(int(x_screen), int(y_screen), 255, 0, 0)

    time.sleep(0.1)

