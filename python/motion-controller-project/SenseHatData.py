from sense_hat import SenseHat
from dataclasses import dataclass
import datetime
import uuid

import DeviceAccelerometerData
import DeviceEnvironmentData
import DeviceGyroscopeData
import DeviceMagnetometerData
import DeviceOrientationData

# dataclass for all the data from the SenseHat
@dataclass
class SenseHatData:
    sessionId: uuid
    timeStamp: datetime