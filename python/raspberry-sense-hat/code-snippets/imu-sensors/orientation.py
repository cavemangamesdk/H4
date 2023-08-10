from sense_hat import SenseHat
import time
import math

sense = SenseHat()

# Disable and re-enable all IMU sensors in order to reset them
sense.set_imu_config(False, False, False)  # Disable all sensors
sense.set_imu_config(True, True, True)  # Enable all sensors

while True:
    orientation = sense.get_orientation()
    orientation_degrees = sense.get_orientation_degrees()
    orientation_radians = sense.get_orientation_radians()

    roll_deg= orientation_degrees['roll']
    pitch_deg  = orientation_degrees['pitch']
    yaw_deg  = orientation_degrees['yaw']

    roll_rad = orientation_radians['roll']
    pitch_rad  = orientation_radians['pitch']
    yaw_rad  = orientation_radians['yaw']

    x = math.cos(yaw_rad) * math.cos(pitch_rad)
    y = math.sin(yaw_rad) * math.cos(pitch_rad)
    z = math.sin(pitch_rad)
    
    # x = round(x, 2)
    # y = round(y, 2)
    # z = round(z, 2)

    # print("roll_deg={0}, pitch_deg={1}, yaw_deg={2}".format(roll_deg, pitch_deg, yaw_deg))
    # print("roll_rad={0}, pitch_rad={1}, yaw_rad={2}".format(roll_rad, pitch_rad, yaw_rad))
    print("x{0}, y={1}, z={2}".format(x, y, z))

    # print(orientation)
    # print(orientation_degrees)
    # print(orientation_radians)

    time.sleep(1)