#
from sense_hat import SenseHat
import datetime
import uuid

# Base data class
from DataClass.DeviceDataBase import DeviceDataBase

# Env sensors
from DataClass.DeviceHumidityData import DeviceHumidityDataBase
from DataClass.DevicePressureData import DevicePressureDataBase

# IMU sensors
from DataClass.DeviceAccelerometerData import DeviceAccelerometerDataBase
from DataClass.DeviceGyroscopeData import DeviceGyroscopeDataBase
from DataClass.DeviceMagnetometerData import DeviceMagnetometerDataBase
from DataClass.DeviceOrientationData import DeviceOrientationDataBase

# Aggregate data classes
from DataClass.DeviceImuData import DeviceImuDataBase
from DataClass.DeviceEnvData import DeviceEnvDataBase

# All data classes
from DataClass.DeviceAllData import DeviceAllDataBase

#
# All data
#

def getAllDataBase(senseHat: SenseHat) -> DeviceAllDataBase:
    
    return DeviceAllDataBase(
        env = getEnvDataBase(senseHat).__dict__,
        imu = getImuDataBase(senseHat).__dict__
    )

def getAllData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceDataBase:
        
    return DeviceDataBase(
        sessionId = str(sessionId),
        timeStamp = str(datetime.datetime.now()),
        data = getAllDataBase(senseHat).__dict__
    )

#
# Aggregate data
#

def getEnvDataBase(senseHat: SenseHat) -> DeviceEnvDataBase:
    
    return DeviceEnvDataBase(
        humidity_sensor = getHumidityDataBase(senseHat).__dict__,
        pressure_sensor = getPressureDataBase(senseHat).__dict__
    )

def getEnvData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceDataBase:
        
    return DeviceDataBase(
        sessionId = str(sessionId),
        timeStamp = str(datetime.datetime.now()),
        data = getEnvDataBase(senseHat).__dict__
    )

def getImuDataBase(senseHat: SenseHat) -> DeviceImuDataBase:
        
    return DeviceImuDataBase(
        accelerometer_sensor = getAccelerometerDataBase(senseHat).__dict__,
        gyroscope_sensor = getGyroscopeDataBase(senseHat).__dict__,
        magnetometer_sensor = getMagnetometerDataBase(senseHat).__dict__,
        orientation_sensor = getOrientationDataBase(senseHat).__dict__
    )

def getImuData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceDataBase:
            
    return DeviceDataBase(
        sessionId = str(sessionId),
        timeStamp = str(datetime.datetime.now()),
        data = getImuDataBase(senseHat).__dict__
    )

#
# Environment data
#

# Humidity
def getHumidityDataBase(senseHat: SenseHat) -> DeviceHumidityDataBase:

    return DeviceHumidityDataBase(
        humidity = senseHat.get_humidity(),
        temperature = senseHat.get_temperature_from_humidity()
    )

def getHumidityData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceDataBase:
    
    return DeviceDataBase(
        sessionId = str(sessionId),
        timeStamp = str(datetime.datetime.now()),
        data = getHumidityDataBase(senseHat).__dict__
    )

# Pressure
def getPressureDataBase(senseHat: SenseHat) -> DevicePressureDataBase:
            
    return DevicePressureDataBase(
        pressure = senseHat.get_pressure(),
        temperature = senseHat.get_temperature_from_pressure() 
    )

def getPressureData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceDataBase:

    return DeviceDataBase(
        sessionId = str(sessionId),
        timeStamp = str(datetime.datetime.now()),
        data = getPressureDataBase(senseHat).__dict__
    )

#
# IMU data
# 

# Acceleration
def getAccelerometerDataBase(senseHat: SenseHat) -> DeviceAccelerometerDataBase:
        
    accel = senseHat.get_accelerometer()
    accelRaw = senseHat.get_accelerometer_raw()

    return DeviceAccelerometerDataBase(
        roll = accel['roll'],
        pitch = accel['pitch'],
        yaw = accel['yaw'],
        x_raw = accelRaw['x'],
        y_raw = accelRaw['y'],
        z_raw = accelRaw['z']
    )

def getAccelerometerData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceDataBase:
    
    return DeviceDataBase(
        sessionId = str(sessionId),
        timeStamp = str(datetime.datetime.now()),
        data = getAccelerometerDataBase(senseHat).__dict__
    )

# Gyroscope
def getGyroscopeDataBase(senseHat: SenseHat) -> DeviceGyroscopeDataBase:
    
    gyro = senseHat.get_gyroscope()
    gyroRaw = senseHat.get_gyroscope_raw()

    return DeviceGyroscopeDataBase(
        roll = gyro['roll'],
        pitch = gyro['pitch'],
        yaw = gyro['yaw'],
        x_raw = gyroRaw['x'],
        y_raw = gyroRaw['y'],
        z_raw = gyroRaw['z']
    )

def getGyroscopeData(senseHat: SenseHat, uuid: uuid.UUID, datetime: datetime) -> DeviceDataBase:
        
    return DeviceDataBase(
        sessionId = str(uuid),
        timeStamp = str(datetime.datetime.now()),
        data = getGyroscopeDataBase(senseHat).__dict__
    )

# Magnetometer
def getMagnetometerDataBase(senseHat: SenseHat) -> DeviceMagnetometerDataBase:
        
    compass = senseHat.get_compass()
    compassRaw = senseHat.get_compass_raw()

    return DeviceMagnetometerDataBase(
        north = compass,
        x_raw = compassRaw['x'],
        y_raw = compassRaw['y'],
        z_raw = compassRaw['z']
    )

def getMagnetometerData(senseHat: SenseHat, uuid: uuid.UUID, datetime: datetime) -> DeviceDataBase:
        
    return DeviceDataBase(
        sessionId = str(uuid),
        timeStamp = str(datetime.datetime.now()),
        data = getMagnetometerDataBase(senseHat).__dict__
    )

# Orientation
def getOrientationDataBase(senseHat: SenseHat) -> DeviceOrientationDataBase:
        
    orientation = senseHat.get_orientation_degrees()
    orientation_rad = senseHat.get_orientation_radians()

    return DeviceOrientationDataBase(
        roll_deg = orientation['roll'],
        pitch_deg = orientation['pitch'],
        yaw_deg = orientation['yaw'],
        roll_rad = orientation_rad['roll'],
        pitch_rad = orientation_rad['pitch'],
        yaw_rad = orientation_rad['yaw']
    )

def getOrientationData(senseHat: SenseHat, uuid: uuid.UUID, datetime: datetime) -> DeviceDataBase:
            
    return DeviceDataBase(
        sessionId = str(uuid),
        timeStamp = str(datetime.datetime.now()),
        data = getOrientationDataBase(senseHat).__dict__
    )