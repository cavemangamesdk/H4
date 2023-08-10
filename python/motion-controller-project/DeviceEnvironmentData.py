from sense_hat import SenseHat
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

def getData(senseHat: SenseHat, uuid: uuid.UUID):
    
    data = DeviceEnvironmentData(
        sessionId = str(uuid),
        timeStamp = str(datetime.datetime.now()),
        temperature = senseHat.get_temperature(),
        humidity = senseHat.get_humidity(),
        pressure = senseHat.get_pressure()
    )

    return data