from dataclasses import dataclass

from DataClass.DeviceDataBase import DeviceDataBase
from DataClass.DeviceAccelerometerData import DeviceAccelerometerDataBase
from DataClass.DeviceGyroscopeData import DeviceGyroscopeDataBase
from DataClass.DeviceMagnetometerData import DeviceMagnetometerDataBase
from DataClass.DeviceOrientationData import DeviceOrientationDataBase

# dataclass for all SenseHat IMU data 
@dataclass
class DeviceImuDataBase():
    accelerometer_sensor: DeviceAccelerometerDataBase.__dict__
    gyroscope_sensor: DeviceGyroscopeDataBase.__dict__
    magnetometer_sensor: DeviceMagnetometerDataBase.__dict__
    orientation_sensor: DeviceOrientationDataBase.__dict__

@dataclass
class DeviceImuData(DeviceDataBase):
    data: DeviceImuDataBase.__dict__