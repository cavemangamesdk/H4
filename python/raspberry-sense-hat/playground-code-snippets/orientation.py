from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    orientation = sense.get_orientation()
    orientation_degrees = sense.get_orientation_degrees()
    orientation_radians = sense.get_orientation_radians()

    # x = orientation_raw['x']
    # y = orientation_raw['y']
    # z = orientation_raw['z']
    
    # x = round(x, 2)
    # y = round(y, 2)
    # z = round(z, 2)

    # print("x={0}, y={1}, z={2}".format(x, y, z))

    print(orientation)
    print(orientation_degrees)
    print(orientation_radians)

    time.sleep(1)