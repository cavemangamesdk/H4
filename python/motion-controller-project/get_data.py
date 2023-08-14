#
from sense_hat import SenseHat
import datetime
import uuid

# Env sensor base classes (without SessionId and TimeStamp)
from DataClass.DeviceHumidityData import DeviceHumidityDataBase
from DataClass.DevicePressureData import DevicePressureDataBase

# Env sensor classes (with SessionId and TimeStamp)
from DataClass.DeviceHumidityData import DeviceHumidityData
from DataClass.DevicePressureData import DevicePressureData

# IMU sensor base classes (without SessionId and TimeStamp)
from DataClass.DeviceAccelerometerData import DeviceAccelerometerDataBase
from DataClass.DeviceGyroscopeData import DeviceGyroscopeDataBase
from DataClass.DeviceMagnetometerData import DeviceMagnetometerDataBase
from DataClass.DeviceOrientationData import DeviceOrientationDataBase

# IMU sensor classes (with SessionId and TimeStamp)
from DataClass.DeviceAccelerometerData import DeviceAccelerometerData
from DataClass.DeviceGyroscopeData import DeviceGyroscopeData
from DataClass.DeviceMagnetometerData import DeviceMagnetometerData
from DataClass.DeviceOrientationData import DeviceOrientationData

# Aggregate data base classes (without SessionId and TimeStamp)
from DataClass.DeviceImuData import DeviceImuDataBase
from DataClass.DeviceEnvData import DeviceEnvDataBase

# Aggregate data classes (with SessionId and TimeStamp)
from DataClass.DeviceImuData import DeviceImuData
from DataClass.DeviceEnvData import DeviceEnvData

# All data class (with SessionId and TimeStamp)
from DataClass.DeviceAllData import Data
from DataClass.DeviceAllData import DeviceAllDataBase
from DataClass.DeviceAllData import DeviceAllData

#
# All data
#

def getAllDataBase(senseHat: SenseHat) -> DeviceAllDataBase:
        
        data = DeviceAllDataBase(
            data = Data(
                getEnvDataBase(senseHat).__dict__,
                getImuDataBase(senseHat).__dict__ ).__dict__
            # env = getEnvDataBase(senseHat).__dict__,
            # imu = getImuDataBase(senseHat).__dict__
    
        )
    
        return data

def getAllData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceAllData:
        
    data = DeviceAllData(
        sessionId = str(sessionId),
        timeStamp = str(datetime.datetime.now()),
        data = Data(
            getEnvDataBase(senseHat).__dict__,
            getImuDataBase(senseHat).__dict__ ).__dict__
        # env = getEnvDataBase(senseHat).__dict__,
        # imu = getImuDataBase(senseHat).__dict__

    )

    return data

#
# Aggregate data
#

def getEnvDataBase(senseHat: SenseHat) -> DeviceEnvDataBase:
    
    data = DeviceEnvDataBase(
        humidity = getHumidityDataBase(senseHat).__dict__,
        pressure = getPressureDataBase(senseHat).__dict__
    )

    return data

def getEnvData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceEnvData:
        
    data = DeviceEnvData(
        sessionId = str(sessionId),
        timeStamp = str(datetime.datetime.now()),
        humidity = getHumidityData(senseHat, sessionId, datetime).__dict__,
        pressure = getPressureData(senseHat, sessionId, datetime).__dict__
    )

    return data

def getImuDataBase(senseHat: SenseHat) -> DeviceImuDataBase:
        
    data = DeviceImuDataBase(
        accelerometer = getAccelerometerDataBase(senseHat).__dict__,
        gyroscope = getGyroscopeDataBase(senseHat).__dict__,
        magnetometer = getMagnetometerDataBase(senseHat).__dict__,
        orientation = getOrientationDataBase(senseHat).__dict__
    )

    return data

def getImuData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceImuData:
            
    data = DeviceImuData(
        sessionId = str(sessionId),
        timeStamp = str(datetime.datetime.now()),
        accelerometer = getAccelerometerData(senseHat, sessionId, datetime).__dict__,
        gyroscope = getGyroscopeData(senseHat, sessionId, datetime).__dict__,
        magnetometer = getMagnetometerData(senseHat, sessionId, datetime).__dict__,
        orientation = getOrientationData(senseHat, sessionId, datetime).__dict__
    )

    return data

#
# Environment data
#

# Humidity
def getHumidityDataBase(senseHat: SenseHat) -> DeviceHumidityDataBase:
        
    humidity = senseHat.get_humidity()
    temperature = senseHat.get_temperature_from_humidity()

    data = DeviceHumidityDataBase(
        humidity = humidity,
        temperature = temperature
    )

    return data

def getHumidityData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceHumidityData:
            
    humidity = senseHat.get_humidity()
    temperature = senseHat.get_temperature_from_humidity()

    data = DeviceHumidityData(
        sessionId = str(sessionId),
        timeStamp = str(datetime.datetime.now()),
        humidity = humidity,
        temperature = temperature
    )

    return data

# Pressure
def getPressureDataBase(senseHat: SenseHat) -> DevicePressureDataBase:
            
    pressure = senseHat.get_pressure()
    temperature = senseHat.get_temperature_from_pressure() 

    data = DevicePressureDataBase(
        pressure = pressure,
        temperature = temperature
    )

    return data

def getPressureData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DevicePressureData:
                    
    pressure = senseHat.get_pressure()
    temperature = senseHat.get_temperature_from_pressure() 

    data = DevicePressureData(
        sessionId = str(sessionId),
        timeStamp = str(datetime.datetime.now()),
        pressure = pressure,
        temperature = temperature
    )

    return data

#
# IMU data
# 

# Acceleration
def getAccelerometerDataBase(senseHat: SenseHat) -> DeviceAccelerometerDataBase:
        
    accel = senseHat.get_accelerometer()
    accelRaw = senseHat.get_accelerometer_raw()

    data = DeviceAccelerometerDataBase(
        roll = accel['roll'],
        pitch = accel['pitch'],
        yaw = accel['yaw'],
        x_raw = accelRaw['x'],
        y_raw = accelRaw['y'],
        z_raw = accelRaw['z']
    )

    return data

def getAccelerometerData(senseHat: SenseHat, sessionId: uuid.UUID, datetime: datetime) -> DeviceAccelerometerData:
        
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

# Gyroscope
def getGyroscopeDataBase(senseHat: SenseHat) -> DeviceGyroscopeDataBase:
    
    gyro = senseHat.get_gyroscope()
    gyroRaw = senseHat.get_gyroscope_raw()

    data = DeviceGyroscopeDataBase(
        roll = gyro['roll'],
        pitch = gyro['pitch'],
        yaw = gyro['yaw'],
        x_raw = gyroRaw['x'],
        y_raw = gyroRaw['y'],
        z_raw = gyroRaw['z']
    )

    return data

def getGyroscopeData(senseHat: SenseHat, uuid: uuid.UUID, datetime: datetime) -> DeviceGyroscopeData:
    
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

# Magnetometer
def getMagnetometerDataBase(senseHat: SenseHat) -> DeviceMagnetometerDataBase:
        
    compass = senseHat.get_compass()
    compassRaw = senseHat.get_compass_raw()

    data = DeviceMagnetometerDataBase(
        north = compass,
        x_raw = compassRaw['x'],
        y_raw = compassRaw['y'],
        z_raw = compassRaw['z']
    )

    return data

def getMagnetometerData(senseHat: SenseHat, uuid: uuid.UUID, datetime: datetime) -> DeviceMagnetometerData:
        
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

# Orientation
def getOrientationDataBase(senseHat: SenseHat) -> DeviceOrientationDataBase:
        
    orientation = senseHat.get_orientation_degrees()
    orientation_rad = senseHat.get_orientation_radians()

    data = DeviceOrientationDataBase(
        roll_deg = orientation['roll'],
        pitch_deg = orientation['pitch'],
        yaw_deg = orientation['yaw'],
        roll_rad = orientation_rad['roll'],
        pitch_rad = orientation_rad['pitch'],
        yaw_rad = orientation_rad['yaw']
    )

    return data

def getOrientationData(senseHat: SenseHat, uuid: uuid.UUID, datetime: datetime) -> DeviceOrientationData:
        
    orientation = senseHat.get_orientation_degrees()
    orientation_rad = senseHat.get_orientation_radians()

    data = DeviceOrientationData(
        sessionId = str(uuid),
        timeStamp = str(datetime.datetime.now()),
        roll_deg = orientation['roll'],
        pitch_deg = orientation['pitch'],
        yaw_deg = orientation['yaw'],
        roll_rad = orientation_rad['roll'],
        pitch_rad = orientation_rad['pitch'],
        yaw_rad = orientation_rad['yaw']
    )

    return data