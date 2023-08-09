from sense_hat import SenseHat
import numpy as np
sense = SenseHat()
sense.clear()

while True:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    
    x = np.cos(yaw)*np.cos(pitch)
    y = np.sin(yaw)*np.cos(pitch)
    z = np.sin(pitch)
    
    print(round(yaw, 0))
    #print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
    #print("x {0} y {1} z {2}".format(x, y, z))