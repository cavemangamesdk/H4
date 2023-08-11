from dataclasses import dataclass

from DataClass.DeviceDataBase import DeviceDataBase
from DataClass.DeviceAccelerometerData import DeviceAccelerometerDataBase
from DataClass.DeviceEnvironmentData import DeviceEnvironmentDataBase
from DataClass.DeviceGyroscopeData import DeviceGyroscopeDataBase
from DataClass.DeviceMagnetometerData import DeviceMagnetometerDataBase
from DataClass.DeviceOrientationData import DeviceOrientationDataBase

# dataclass for all the data from the SenseHat
@dataclass
class DeviceAllDataBase():
    accelerometer: DeviceAccelerometerDataBase.__dict__
    environment: DeviceEnvironmentDataBase.__dict__
    gyroscope: DeviceGyroscopeDataBase.__dict__
    magnetometer: DeviceMagnetometerDataBase.__dict__
    orientation: DeviceOrientationDataBase.__dict__

@dataclass
class DeviceAllData(DeviceDataBase, DeviceAllDataBase):
    pass

# @dataclass
# class DeviceAllData(DeviceData):
#     # from get_accelerometer()
#     roll: float
#     pitch: float
#     yaw: float
#     # from get_accelerometer_raw()
#     x_raw: float
#     y_raw: float
#     z_raw: float
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
#     # from get_gyroscope()
#     roll: float
#     pitch: float
#     yaw: float
#     # from get_gyroscope_raw()
#     x_raw: float
#     y_raw: float
#     z_raw: float
#     # from get_compass()
#     compass: float
#     # from get_compass_raw()
#     x_raw: float
#     y_raw: float
#     z_raw: float
#     # from get_orientation()
#     roll: float
#     pitch: float
#     yaw: float
#     # from get_orientation_radians()
#     roll: float
#     pitch: float
#     yaw: float
