from sense_hat import SenseHat
from dataclasses import dataclass
import datetime
import uuid

@dataclass
class DeviceEnvironmentData:
    sessionId: uuid
    timeStamp: datetime
    temperature: float
    temperatureFromHumidity: float
    temperatureFromPressure: float
    humidity: float
    pressure: float

def getData(senseHat: SenseHat, uuid: uuid.UUID, datetime: datetime):
    
    data = DeviceEnvironmentData(
        sessionId = str(uuid),
        timeStamp = str(datetime.datetime.now()),
        temperature = senseHat.get_temperature(),
        temperatureFromHumidity = senseHat.get_temperature_from_humidity(),
        temperatureFromPressure = senseHat.get_temperature_from_pressure(),
        humidity = senseHat.get_humidity(),
        pressure = senseHat.get_pressure()
    )

    return data