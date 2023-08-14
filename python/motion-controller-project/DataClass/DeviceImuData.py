from dataclasses import dataclass

from DataClass.DeviceDataBase import DeviceDataBase
from DataClass.DeviceAccelerometerData import DeviceAccelerometerDataBase
from DataClass.DeviceGyroscopeData import DeviceGyroscopeDataBase
from DataClass.DeviceMagnetometerData import DeviceMagnetometerDataBase
from DataClass.DeviceOrientationData import DeviceOrientationDataBase

# dataclass for all SenseHat IMU data 
@dataclass
class DeviceImuDataBase():
    accelerometer: DeviceAccelerometerDataBase.__dict__
    gyroscope: DeviceGyroscopeDataBase.__dict__
    magnetometer: DeviceMagnetometerDataBase.__dict__
    orientation: DeviceOrientationDataBase.__dict__

@dataclass
class DeviceImuData(DeviceDataBase, DeviceImuDataBase):
    pass