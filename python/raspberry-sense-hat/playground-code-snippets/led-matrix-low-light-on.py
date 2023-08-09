import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear(0, 48, 48)

print(sense.gamma)
time.sleep(2)

sense.gamma = reversed(sense.gamma)
print(sense.gamma)
time.sleep(2)

sense.low_light = True
print(sense.gamma)
time.sleep(2)

sense.low_light = False