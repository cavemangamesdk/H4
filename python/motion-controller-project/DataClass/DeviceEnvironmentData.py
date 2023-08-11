from dataclasses import dataclass
from DataClass.DeviceDataBase import DeviceDataBase

@dataclass
class DeviceEnvironmentDataBase():
    temperature: float
    temperatureFromHumidity: float
    temperatureFromPressure: float
    humidity: float
    pressure: float

@dataclass
class DeviceEnvironmentData(DeviceDataBase, DeviceEnvironmentDataBase):
    pass