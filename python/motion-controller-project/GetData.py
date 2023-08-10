from sense_hat import SenseHat
import datetime
import uuid

from DataClass.DeviceAccelerometerData import DeviceAccelerometerData
from DataClass.DeviceEnvironmentData import DeviceEnvironmentData
from DataClass.DeviceGyroscopeData import DeviceGyroscopeData
from DataClass.DeviceMagnetometerData import DeviceMagnetometerData
from DataClass.DeviceOrientationData import DeviceOrientationData

#
def getAccelerometerData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime):
        
    accel = senseHat.get_accelerometer()
    accelRaw = senseHat.get_accelerometer_raw()

    data = DeviceAccelerometerData(
        sessionId = str(sessionId),
        timeStamp = str(datetime.datetime.now()),
        roll = accel['roll'],
        pitch = accel['pitch'],
        yaw = accel['yaw'],
        x_raw = accelRaw['x'],
        y_raw = accelRaw['y'],
        z_raw = accelRaw['z']
    )

    return data

def getEnvironmentData(senseHat: SenseHat, uuid: uuid.UUID, datetime: datetime):
    
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

def getGyroscopeData(senseHat: SenseHat, uuid: uuid.UUID, datetime: datetime):
    
    gyro = senseHat.get_gyroscope()
    gyroRaw = senseHat.get_gyroscope_raw()

    data = DeviceGyroscopeData(
        sessionId = str(uuid),
        timeStamp = str(datetime.datetime.now()),
        roll = gyro['roll'],
        pitch = gyro['pitch'],
        yaw = gyro['yaw'],
        x_raw = gyroRaw['x'],
        y_raw = gyroRaw['y'],
        z_raw = gyroRaw['z']
    )

    return data

def getMagnetometerData(senseHat: SenseHat, uuid: uuid.UUID, datetime: datetime):
        
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

def getOrientationData(senseHat: SenseHat, uuid: uuid.UUID, datetime: datetime):
        
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