from dataclasses import dataclass
import datetime
import uuid

@dataclass
class DeviceDataBase:
    sessionId: uuid
    timeStamp: datetime
    data: dict