#from sense_hat import SenseHat
import math
import time

#sense = SenseHat()

x = 0
y = 0

# variable holding the 8x8 led matrix screen
screen = [[48, 48, 48] for x in range(64)]

# Function setPixel that writes to screen variable
def setPixel(screen, x, y, r, g, b):
    screen[int(x) + int(y) * 8] = [r, g, b]

# Function setPixelFrac that writes to screen variable
def setPixelFrac(screen, x, y, r, g, b):
    # Calculate the weights for the neighboring pixels
    x1, x_frac = divmod(x, 1)
    y1, y_frac = divmod(y, 1)
    x1, y1 = int(x1), int(y1)
    weights = [(1 - x_frac) * (1 - y_frac), x_frac * (1 - y_frac), (1 - x_frac) * y_frac, x_frac * y_frac]

    # Calculate the colors for the neighboring pixels
    colors = [screen[x1 + dx + (y1 + dy) * 8] for dx, dy in [(0, 0), (1, 0), (0, 1), (1, 1)]]
    colors = [[int(c + w * color) for c, color in zip(cs, (r, g, b))] for w, cs in zip(weights, colors)]

    # Set the colors of the neighboring pixels
    for (dx, dy), color in zip([(0, 0), (1, 0), (0, 1), (1, 1)], colors):
        screen[x1 + dx + (y1 + dy) * 8] = color

while True:

    x += 0.07
    y += 0.07

    x_screen = (3.5 + math.sin(x) * 4)
    y_screen = (3.5 + math.cos(y) * 4)

    # 
    screen = [[48, 48, 48] for x in range(64)]

    # print(x_screen, y_screen)

    #sense.clear(48, 48, 48)

    #sense.set_pixel(x_screen, y_screen, 255, 255, 0)

    setPixelFrac(screen, x, y, 255, 255, 0)

    print(screen) 

    time.sleep(1)
    #time.sleep(60/1000)

