from dataclasses import dataclass
from DeviceData import DeviceData

@dataclass
class DeviceEnvironmentData(DeviceData):
    temperature: float
    temperatureFromHumidity: float
    temperatureFromPressure: float
    humidity: float
    pressure: float