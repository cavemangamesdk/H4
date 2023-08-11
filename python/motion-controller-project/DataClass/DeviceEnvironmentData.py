from dataclasses import dataclass
from DataClass.DeviceData import DeviceData

@dataclass
class DeviceEnvironmentDataBase():
    temperature: float
    temperatureFromHumidity: float
    temperatureFromPressure: float
    humidity: float
    pressure: float

@dataclass
class DeviceEnvironmentData(DeviceData, DeviceEnvironmentDataBase):
    pass