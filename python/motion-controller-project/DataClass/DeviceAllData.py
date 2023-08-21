from dataclasses import dataclass

from DataClass.DeviceDataBase import DeviceDataBase
from DataClass.DeviceEnvData import DeviceEnvDataBase
from DataClass.DeviceImuData import DeviceImuDataBase

# dataclass for all the data from the SenseHat
@dataclass
class DeviceAllDataBase():
    env: DeviceEnvDataBase.__dict__
    imu: DeviceImuDataBase.__dict__

@dataclass
class DeviceAllData(DeviceDataBase):
    data: DeviceAllDataBase.__dict__
