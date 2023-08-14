from dataclasses import dataclass
from DataClass.DeviceDataBase import DeviceDataBase
from DataClass.DeviceHumidityData import DeviceHumidityDataBase
from DataClass.DevicePressureData import DevicePressureDataBase

# Dataclass for all Sense Hat environment sensors
@dataclass
class DeviceEnvDataBase():
    humidity: DeviceHumidityDataBase.__dict__
    pressure: DevicePressureDataBase.__dict__

@dataclass
class DeviceEnvData(DeviceDataBase):
    data: DeviceEnvDataBase.__dict__
    

# from dataclasses import dataclass
# from DataClass.DeviceDataBase import DeviceDataBase

# @dataclass
# class DeviceEnvironmentDataBase():
#     # from get_temperature()
#     temperature: float
#     # from get_temperature_from_humidity()
#     temperatureFromHumidity: float
#     # from get_temperature_from_pressure()
#     temperatureFromPressure: float
#     # from get_humidity()
#     humidity: float
#     # from get_pressure()
#     pressure: float

# @dataclass
# class DeviceEnvironmentData(DeviceDataBase, DeviceEnvironmentDataBase):
#     pass