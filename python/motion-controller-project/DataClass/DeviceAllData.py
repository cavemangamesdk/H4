from dataclasses import dataclass
from DataClass.DeviceData import DeviceData
from DataClass.DeviceAccelerometerData import DeviceAccelerometerData
from DataClass.DeviceEnvironmentData import DeviceEnvironmentData
from DataClass.DeviceGyroscopeData import DeviceGyroscopeData
from DataClass.DeviceMagnetometerData import DeviceMagnetometerData
from DataClass.DeviceOrientationData import DeviceOrientationData

# dataclass for all the data from the SenseHat
@dataclass
class DeviceAllData(DeviceData):
    accelerometer: DeviceAccelerometerData.__dict__
    environment: DeviceEnvironmentData.__dict__
    gyroscope: DeviceGyroscopeData.__dict__
    magnetometer: DeviceMagnetometerData.__dict__
    orientation: DeviceOrientationData.__dict__

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
