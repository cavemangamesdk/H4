import time
from sense_hat import SenseHat

sense = SenseHat()

sense.clear(0, 0, 0)

pixels = [[x]*3 for x in range(64)]
gamma = [x for x in range(32)]

print(pixels)
print(gamma)

# sense.gamma = gamma

sense.set_pixel = pixels

# print(sense.gamma)
# time.sleep(2)

#sense.gamma = [31] * 32 #reversed(sense.gamma)
#sense.gamma = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
# time.sleep(2)
# print(sense.gamma)
# time.sleep(2)

# sense.low_light = True
# print(sense.gamma)
# time.sleep(2)

# sense.low_light = False
# print(sense.gamma)
# time.sleep(2)