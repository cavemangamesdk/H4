from sense_hat import SenseHat
from dataclasses import dataclass
import datetime
import uuid

@dataclass
class DeviceMagnetometerData:
    sessionId: uuid
    timeStamp: datetime
    # from get_compass()
    north: float
    # from get_compass_raw()
    x_raw: float
    y_raw: float
    z_raw: float

def getData(senseHat: SenseHat, uuid: uuid.UUID, datetime: datetime):
        
    compass = senseHat.get_compass()
    compassRaw = senseHat.get_compass_raw()

    data = DeviceMagnetometerData(
        sessionId = str(uuid),
        timeStamp = str(datetime.datetime.now()),
        north = compass,
        x_raw = compassRaw['x'],
        y_raw = compassRaw['y'],
        z_raw = compassRaw['z']
    )

    return data