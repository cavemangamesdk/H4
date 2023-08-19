#
import board # pip3 install adafruit-blinka
import adafruit_bno055 # pip3 install adafruit-circuitpython-bno055 (NOT adafruit-bno055)
# import datetime
# import uuid

# #  data class
# from DataClass_BNO055.Base import Base

# # IMU sensors
# from DataClass_BNO055.Acceleration import Acceleration
# from DataClass_BNO055.Gyroscope import Gyroscope
# from DataClass_BNO055.Magnetometer import Magnetometer
# from DataClass_BNO055.Euler import Euler
# from DataClass_BNO055.Quaternion import Quaternion
# from DataClass_BNO055.LinearAcceleration import LinearAcceleration
# from DataClass_BNO055.Gravity import Gravity
# from DataClass_BNO055.Temperature import Temperature


#
i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c, address=0x29)

#
def getPitchRollData(sensor: adafruit_bno055.BNO055_I2C) -> str:
            
    euler = sensor.euler
    #gyro = bno_055.get_gyroscope()

    #return f"{round(orientation['roll'], 2)}, {round(orientation['pitch'], 2)}, {round(gyro['yaw'], 2)}"
    return f"{euler[0]}, {euler[1]}, {euler[2]}"