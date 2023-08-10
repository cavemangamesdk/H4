# Device data base class

from dataclasses import dataclass
import datetime
import uuid

@dataclass
class DeviceData:
    sessionId: uuid
    timeStamp: datetime