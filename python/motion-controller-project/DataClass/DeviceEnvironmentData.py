from dataclasses import dataclass
from DataClass.DeviceData import DeviceData

@dataclass
class DeviceEnvironmentData(DeviceData):
    temperature: float
    temperatureFromHumidity: float
    temperatureFromPressure: float
    humidity: float
    pressure: float