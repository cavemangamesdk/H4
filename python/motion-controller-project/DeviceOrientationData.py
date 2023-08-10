from sense_hat import SenseHat
from dataclasses import dataclass
import datetime
import uuid

@dataclass
class DeviceOrientationData:
    sessionId: uuid
    timeStamp: datetime
    # from gett_orientation_degrees()
    roll_deg: float
    pitch_deg: float
    yaw_deg: float
    # from get_orientation_radians()
    roll_rad: float
    pitch_rad: float
    yaw_rad: float

def getData(senseHat: SenseHat, uuid: uuid.UUID):
        
    orientation = senseHat.get_orientation_degrees()
    orientationRad = senseHat.get_orientation_radians()

    data = DeviceOrientationData(
        sessionId = str(uuid),
        timeStamp = str(datetime.datetime.now()),
        roll_deg = orientation['roll'],
        pitch_deg = orientation['pitch'],
        yaw_deg = orientation['yaw'],
        roll_rad = orientationRad['roll'],
        pitch_rad = orientationRad['pitch'],
        yaw_rad = orientationRad['yaw']
    )

    return data
