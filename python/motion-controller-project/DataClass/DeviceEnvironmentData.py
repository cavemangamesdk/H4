from dataclasses import dataclass
from DataClass.DeviceDataBase import DeviceDataBase

@dataclass
class DeviceEnvironmentDataBase():
    # from get_temperature()
    temperature: float
    # from get_temperature_from_humidity()
    temperatureFromHumidity: float
    # from get_temperature_from_pressure()
    temperatureFromPressure: float
    # from get_humidity()
    humidity: float
    # from get_pressure()
    pressure: float

@dataclass
class DeviceEnvironmentData(DeviceDataBase, DeviceEnvironmentDataBase):
    pass