from sense_hat import SenseHat
import math
import time

sense = SenseHat()

x = 0
y = 0

while True:

    x += 0.07
    y += 0.07

    x_screen = round(3.5 + math.sin(x) * 4)
    y_screen = x_screen #round(3.5 + math.cos(y) * 4)

    # print(x_screen, y_screen)

    sense.clear(48, 48, 48)

    sense.set_pixel(x_screen, y_screen, 255, 255, 0)

    time.sleep(60/1000)

