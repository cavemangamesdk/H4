#
from sense_hat import SenseHat
import datetime
import uuid

# Env sensors
from DataClass.DeviceHumidityData import DeviceHumidityDataBase, DeviceHumidityData
from DataClass.DevicePressureData import DevicePressureDataBase, DevicePressureData

# IMU sensors
from DataClass.DeviceAccelerometerData import DeviceAccelerometerDataBase, DeviceAccelerometerData
from DataClass.DeviceGyroscopeData import DeviceGyroscopeDataBase, DeviceGyroscopeData
from DataClass.DeviceMagnetometerData import DeviceMagnetometerDataBase, DeviceMagnetometerData
from DataClass.DeviceOrientationData import DeviceOrientationDataBase, DeviceOrientationData

# Aggregate data classes
from DataClass.DeviceImuData import DeviceImuDataBase, DeviceImuData
from DataClass.DeviceEnvData import DeviceEnvDataBase, DeviceEnvData

# All data classes
from DataClass.DeviceAllData import DeviceAllDataBase, DeviceAllData

#
# All data
#

def getAllDataBase(senseHat: SenseHat) -> DeviceAllDataBase:
    
    return DeviceAllDataBase(
        env = getEnvDataBase(senseHat).__dict__,
        imu = getImuDataBase(senseHat).__dict__
    )

def getAllData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceAllData:
        
    return DeviceAllData(
        sessionId = str(sessionId),
        timeStamp = str(datetime.datetime.now()),
        data = getAllDataBase(senseHat).__dict__
    )

#
# Aggregate data
#

def getEnvDataBase(senseHat: SenseHat) -> DeviceEnvDataBase:
    
    return DeviceEnvDataBase(
        humidity = getHumidityDataBase(senseHat).__dict__,
        pressure = getPressureDataBase(senseHat).__dict__
    )

def getEnvData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceEnvData:
        
    return DeviceEnvData(
        sessionId = str(sessionId),
        timeStamp = str(datetime.datetime.now()),
        data = getEnvDataBase(senseHat).__dict__
    )

def getImuDataBase(senseHat: SenseHat) -> DeviceImuDataBase:
        
    return DeviceImuDataBase(
        accelerometer = getAccelerometerDataBase(senseHat).__dict__,
        gyroscope = getGyroscopeDataBase(senseHat).__dict__,
        magnetometer = getMagnetometerDataBase(senseHat).__dict__,
        orientation = getOrientationDataBase(senseHat).__dict__
    )

def getImuData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceImuData:
            
    return DeviceImuData(
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

def getHumidityData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceHumidityData:
    
    return DeviceHumidityData(
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

def getPressureData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DevicePressureData:

    return DevicePressureData(
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

def getAccelerometerData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceAccelerometerData:
    
    return DeviceAccelerometerData(
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

def getGyroscopeData(senseHat: SenseHat, uuid: uuid.UUID, datetime: datetime) -> DeviceGyroscopeData:
        
    return DeviceGyroscopeData(
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

def getMagnetometerData(senseHat: SenseHat, uuid: uuid.UUID, datetime: datetime) -> DeviceMagnetometerData:
        
    return DeviceMagnetometerData(
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

def getOrientationData(senseHat: SenseHat, uuid: uuid.UUID, datetime: datetime) -> DeviceOrientationData:
            
    return DeviceOrientationData(
        sessionId = str(uuid),
        timeStamp = str(datetime.datetime.now()),
        data = getOrientationDataBase(senseHat).__dict__
    )