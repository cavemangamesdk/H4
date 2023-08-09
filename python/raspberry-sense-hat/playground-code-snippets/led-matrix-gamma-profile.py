from sense_hat import SenseHat
sense = SenseHat()

#print(type(sense.gamma))

pixels = [[x]*3 for x in range(64)]

print(pixels)

sense.set_pixels(pixels)