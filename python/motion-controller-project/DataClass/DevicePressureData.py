from dataclasses import dataclass
from DataClass.DeviceDataBase import DeviceDataBase

@dataclass
class DevicePressureDataBase():
    # from get_pressure()
    pressure: float
    # from get_temperature_from_pressure()
    temperature: float

@dataclass
class DevicePressureData(DeviceDataBase):
    data: DevicePressureDataBase.__dict__