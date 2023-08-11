from dataclasses import dataclass
from DeviceData import DeviceData
from DeviceAccelerometerData import DeviceAccelerometerData
from DeviceEnvironmentData import DeviceEnvironmentData
from DeviceGyroscopeData import DeviceGyroscopeData
from DeviceMagnetometerData import DeviceMagnetometerData
from DeviceOrientationData import DeviceOrientationData

# dataclass for all the data from the SenseHat
@dataclass
class DeviceAllData(DeviceData):
    accelerometer: DeviceAccelerometerData
    environment: DeviceEnvironmentData
    gyroscope: DeviceGyroscopeData
    magnetometer: DeviceMagnetometerData
    orientation: DeviceOrientationData

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
