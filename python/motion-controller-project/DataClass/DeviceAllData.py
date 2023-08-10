from dataclasses import dataclass
from DeviceAccelerometerData import DeviceAccelerometerData
from DeviceEnvironmentData import DeviceEnvironmentData
from DeviceGyroscopeData import DeviceGyroscopeData
from DeviceMagnetometerData import DeviceMagnetometerData
from DeviceOrientationData import DeviceOrientationData

# dataclass for all the data from the SenseHat
@dataclass
class DeviceAllData(DeviceAccelerometerData, DeviceEnvironmentData, DeviceGyroscopeData, DeviceMagnetometerData, DeviceOrientationData):
    pass