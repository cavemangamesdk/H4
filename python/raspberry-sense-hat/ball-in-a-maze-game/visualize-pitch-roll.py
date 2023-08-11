from sense_hat import SenseHat
import time

sense = SenseHat()

sense.low_light = True

while True:

    # Get the raw gyro values
    raw = sense.get_gyroscope_raw()
    
    # pitch = sense.get_orientation_radians()['pitch']
    # roll = sense.get_orientation_radians()['roll']
    
    # print("pitch {0} roll {1}".format(pitch, roll))
    
    # pitch_color = abs(int(pitch / (3.14 / 2) * 255))
    # roll_color = abs(int(roll / (3.14 / 2) * 255))

    # sense.set_pixel(0, 0, (pitch_color, 0, 0))
    # sense.set_pixel(7, 7, (0, 0, roll_color))

    time.sleep(0.2)
    
