from dataclasses import dataclass
import datetime
import uuid

@dataclass
class DeviceEnvironmentData:
    sessionId: uuid
    timeStamp: datetime
    temperature: float
    humidity: float
    pressure: float