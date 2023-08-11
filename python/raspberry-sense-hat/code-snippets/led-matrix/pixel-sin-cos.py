#from sense_hat import SenseHat
import math
import time

#sense = SenseHat()

x = 1
y = 1

while True:

    x += 0.11
    y += 0.11

    x_screen = int(4.5 + math.sin(x) * 4)
    y_screen = int(4.5 + math.cos(y) * 4)

    print(x_screen, y_screen)

    #sense.clear(0, 0, 0)

    #sense.set_pixel(int(x_screen), int(y_screen), 255, 0, 0)

    time.sleep(0.1)

