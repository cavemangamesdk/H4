# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board # pip3 install adafruit-blinka
# import Adafruit_BNO055 # pip3 install adafruit_bno055   
from Adafruit_BNO055 import BNO055

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = BNO055.BNO055(rst=18)

# If you are going to use UART uncomment these lines
# uart = board.UART()
# sensor = adafruit_bno055.BNO055_UART(uart)

last_val = 0xFFFF

def temperature():
    global last_val  # pylint: disable=global-statement
    result = sensor.read_temp()
    if abs(result - last_val) == 128:
        result = sensor.read_temp()
        if abs(result - last_val) == 128:
            return 0b00111111 & result
    last_val = result
    return result

while True:
    print("Temperature: {} degrees C".format(sensor.read_temp()))
    """
    print(
        "Temperature: {} degrees C".format(temperature())
    )  # Uncomment if using a Raspberry Pi
    """
    print("Accelerometer (m/s^2): {}".format(sensor.read_accelerometer()))
    print("Magnetometer (microteslas): {}".format(sensor.read_magnetometer()))
    print("Gyroscope (rad/sec): {}".format(sensor.read_gyroscope()))
    print("Euler angle: {}".format(sensor.read_euler()))
    print("Quaternion: {}".format(sensor.read_quaternion()))
    print("Linear acceleration (m/s^2): {}".format(sensor.read_linear_acceleration()))
    print("Gravity (m/s^2): {}".format(sensor.read_gravity()))
    print()

    time.sleep(1)
