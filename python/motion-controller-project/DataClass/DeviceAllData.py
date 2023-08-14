from dataclasses import dataclass

from DataClass.DeviceDataBase import DeviceDataBase
from DataClass.DeviceEnvData import DeviceEnvDataBase
from DataClass.DeviceImuData import DeviceImuDataBase

@dataclass
class Data():
    env: DeviceEnvDataBase.__dict__
    imu: DeviceImuDataBase.__dict__

# dataclass for all the data from the SenseHat
@dataclass
class DeviceAllDataBase():
    data: Data.__dict__
    # env: DeviceEnvDataBase.__dict__
    # imu: DeviceImuDataBase.__dict__

@dataclass
class DeviceAllData(DeviceDataBase, DeviceAllDataBase):
    pass

# from dataclasses import dataclass

# from DataClass.DeviceDataBase import DeviceDataBase
# from DataClass.DeviceAccelerometerData import DeviceAccelerometerDataBase
# from DataClass.DeviceEnvironmentData import DeviceEnvironmentDataBase
# from DataClass.DeviceGyroscopeData import DeviceGyroscopeDataBase
# from DataClass.DeviceMagnetometerData import DeviceMagnetometerDataBase
# from DataClass.DeviceOrientationData import DeviceOrientationDataBase

# # dataclass for all the data from the SenseHat
# @dataclass
# class DeviceAllDataBase():
#     accelerometer: DeviceAccelerometerDataBase.__dict__
#     environment: DeviceEnvironmentDataBase.__dict__
#     gyroscope: DeviceGyroscopeDataBase.__dict__
#     magnetometer: DeviceMagnetometerDataBase.__dict__
#     orientation: DeviceOrientationDataBase.__dict__

# @dataclass
# class DeviceAllData(DeviceDataBase, DeviceAllDataBase):
#     pass