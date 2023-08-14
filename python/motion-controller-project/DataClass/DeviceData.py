from dataclasses import dataclass
from DataClass.DeviceDataBase import DeviceDataBase

@dataclass
class DeviceData(DeviceDataBase):
    data: dict