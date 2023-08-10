from dataclasses import dataclass
import datetime
import uuid

@dataclass
class DeviceEnvironmentData:
    deviceId: uuid
    timeStamp: datetime
    temperature: float
    humidity: float
    pressure: float