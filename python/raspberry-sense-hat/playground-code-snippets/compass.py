from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    compass = sense.get_compass()
    compass_raw = sense.get_compass_raw()

    x = compass_raw['x']
    y = compass_raw['y']
    z = compass_raw['z']

    x = round(x, 2)
    y = round(y, 2)
    z = round(z, 2)

    print("x={0}, y={1}, z={2}".format(x, y, z))

    print(compass)

    time.sleep(1)