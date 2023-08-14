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

@dataclass
class DeviceAllData(DeviceDataBase, DeviceAllDataBase):
    pass
