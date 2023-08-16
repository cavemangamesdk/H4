from sense_hat import SenseHat

sense = SenseHat()

sense.low_light = True

r = (128, 0, 0)
b = (0, 0, 0)
w = (255, 255, 255)

# marble
x = 1
y = 1

maze = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,b,r,b,b,r],
        [r,b,r,b,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,b,r,r,r,r,b,r],
        [r,b,b,r,b,b,b,r],
        [r,r,r,r,r,r,r,r]]

sense.set_pixels(sum(maze,[]))

sense.set_pixel(x, y, w)