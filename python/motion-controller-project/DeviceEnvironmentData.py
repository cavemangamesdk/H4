from dataclasses import dataclass
import datetime

@dataclass
class DeviceEnvironmentData:
    timeStamp: datetime
    temperature: float
    humidity: float
    pressure: float