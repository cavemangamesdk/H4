from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    gyroscope = sense.get_gyroscope()
    gyroscope_raw = sense.get_gyroscope_raw()

    roll = gyroscope['roll']
    pitch = gyroscope['pitch']
    yaw  = gyroscope['yaw']

    x_raw = gyroscope_raw['x'] 
    y_raw  = gyroscope_raw['y']
    z_raw  = gyroscope_raw['z']

    roll = round(roll, 2)
    pitch = round(pitch, 2)
    yaw = round(yaw, 2)



    print("x={0}, y={1}, z={2}".format(x_raw, y_raw, z_raw))

    print("roll={0}, pitch={1}, yaw={2}".format(roll, pitch , yaw))

    time.sleep(1)