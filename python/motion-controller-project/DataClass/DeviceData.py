from dataclasses import dataclass
import datetime
import uuid

@dataclass
class DeviceData:
    sessionId: uuid
    timeStamp: datetime