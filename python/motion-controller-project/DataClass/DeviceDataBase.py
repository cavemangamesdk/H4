from dataclasses import dataclass
import datetime
import uuid

@dataclass
class DeviceDataBase:
    session_id: uuid
    timestamp: datetime
    data: dict