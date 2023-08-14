from dataclasses import dataclass
from DataClass.DeviceDataBase import DeviceDataBase

@dataclass
class DeviceHumidityDataBase():
    # from get_humidity()
    humidity: float
    # from get_temperature_from_humidity()
    temperature: float

@dataclass
class DeviceHumidityData(DeviceDataBase, DeviceHumidityDataBase):
    pass