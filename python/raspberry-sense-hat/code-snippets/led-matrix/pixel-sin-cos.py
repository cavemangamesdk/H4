#from sense_hat import SenseHat
import math
import time

#sense = SenseHat()

x = 1
y = 1

# variable holding the 8x8 led matrix screen
screen = [[48, 48, 48] for x in range(64)]

# Function setPixel that writes to screen buffer
def setPixel(screen, x, y, r, g, b):
    screen[int(x) + int(y) * 8] = [r, g, b]

def getPixel(screen, x, y):
    return screen[int(x) + int(y) * 8]

def addPixel(screen, x, y, r, g, b):

    r_new = r + getPixel(screen, x, y)[0]
    g_new = g + getPixel(screen, x, y)[1]
    b_new = b + getPixel(screen, x, y)[2]

    # cap values at 255
    if r_new > 255:
        r_new = 255
    if g_new > 255:
        g_new = 255
    if b_new > 255:
        b_new = 255
    
    # convert values to int and write to buffer using setPixel function
    setPixel(screen, x, y, int(r_new), int(g_new), int(b_new))

# function setPixelSmooth that writes to screen variable
def setPixelSmooth(screen, x, y, r, g, b):
    x_frac, x_int = math.modf(x)
    y_frac, y_int = math.modf(y)

    addPixel(screen, x_int, y_int, r * (1 - x_frac) * (1 - y_frac), g * (1 - x_frac) * (1 - y_frac), b * (1 - x_frac) * (1 - y_frac))
    addPixel(screen, x_int + 1, y_int, r * x_frac * (1 - y_frac), g * x_frac * (1 - y_frac), b * x_frac * (1 - y_frac))
    addPixel(screen, x_int, y_int + 1, r * (1 - x_frac) * y_frac, g * (1 - x_frac) * y_frac, b * (1 - x_frac) * y_frac)
    addPixel(screen, x_int + 1, y_int + 1, r * x_frac * y_frac, g * x_frac * y_frac, b * x_frac * y_frac)


while True:

    x += 0.07
    y += 0.07

    x_screen = 3.5 + math.sin(x) * 4
    y_screen = 3.5 + math.cos(y) * 4

    # Reset the screen
    screen = [[48, 48, 48] for x in range(64)]

    setPixelSmooth(screen, x_screen, y_screen, 0, 0, 255)

    print(screen)

    #sense.set_pixels(screen)

    time.sleep(1)
    #time.sleep(60/1000)