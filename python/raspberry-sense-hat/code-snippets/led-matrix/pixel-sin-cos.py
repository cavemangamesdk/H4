from sense_hat import SenseHat
import math
import time

sense = SenseHat()

x = 1
y = 1

# variable holding the 8x8 led matrix screen
screen = [[48, 48, 48] for x in range(64)]

# Function setPixel that writes to screen variable
def setPixel(screen, x, y, r, g, b):
    screen[int(x) + int(y) * 8] = [r, g, b]

# function setPixelSmooth that writes to screen variable
# and uses subpixel rendering
def setPixelSmooth(screen, x, y, r, g, b):
    x_frac, x_int = math.modf(x)
    y_frac, y_int = math.modf(y)


while True:

    x += 0.07
    y += 0.07

    x_screen = (3.5 + math.sin(x) * 4)
    y_screen = (3.5 + math.cos(y) * 4)

    # Reset the screen
    screen = [[48, 48, 48] for x in range(64)]

    setPixel(screen, x, y, 0, 0, 255)

    print(screen)

    sense.set_pixels(screen)

    time.sleep(1)
    #time.sleep(60/1000)