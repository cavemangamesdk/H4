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

# Unity specific
from DataClass.DeviceOrientationPitchRollData import DeviceOrientationPitchRollData

# Aggregate data classes
from DataClass.DeviceImuData import DeviceImuDataBase
from DataClass.DeviceEnvData import DeviceEnvDataBase

# All data classes
from DataClass.DeviceAllData import DeviceAllDataBase

#
# All data
#

def getAllDataBase(sense_hat: SenseHat) -> DeviceAllDataBase:
    
    return DeviceAllDataBase(
        env = getEnvDataBase(sense_hat).__dict__,
        imu = getImuDataBase(sense_hat).__dict__
    )

def getAllData(sense_hat: SenseHat, session_id: uuid.UUID, datetime: datetime) -> DeviceDataBase:
        
    return DeviceDataBase(
        session_id = str(session_id),
        timestamp = str(datetime.datetime.now()),
        data = getAllDataBase(sense_hat).__dict__
    )

#
# Aggregate data
#

def getEnvDataBase(sense_hat: SenseHat) -> DeviceEnvDataBase:
    
    return DeviceEnvDataBase(
        humidity_sensor = getHumidityDataBase(sense_hat).__dict__,
        pressure_sensor = getPressureDataBase(sense_hat).__dict__
    )

def getEnvData(sense_hat: SenseHat, session_id: uuid.UUID, datetime: datetime) -> DeviceDataBase:
        
    return DeviceDataBase(
        session_id = str(session_id),
        timestamp = str(datetime.datetime.now()),
        data = getEnvDataBase(sense_hat).__dict__
    )

def getImuDataBase(sense_hat: SenseHat) -> DeviceImuDataBase:
        
    return DeviceImuDataBase(
        accelerometer_sensor = getAccelerometerDataBase(sense_hat).__dict__,
        gyroscope_sensor = getGyroscopeDataBase(sense_hat).__dict__,
        magnetometer_sensor = getMagnetometerDataBase(sense_hat).__dict__,
        orientation_sensor = getOrientationDataBase(sense_hat).__dict__
    )

def getImuData(sense_hat: SenseHat, session_id: uuid.UUID, datetime: datetime) -> DeviceDataBase:
            
    return DeviceDataBase(
        session_id = str(session_id),
        timestamp = str(datetime.datetime.now()),
        data = getImuDataBase(sense_hat).__dict__
    )

#
# Environment data
#

# Humidity
def getHumidityDataBase(sense_hat: SenseHat) -> DeviceHumidityDataBase:

    return DeviceHumidityDataBase(
        humidity = sense_hat.get_humidity(),
        temperature = sense_hat.get_temperature_from_humidity()
    )

def getHumidityData(sense_hat: SenseHat, session_id: uuid.UUID, datetime: datetime) -> DeviceDataBase:
    
    return DeviceDataBase(
        session_id = str(session_id),
        timestamp = str(datetime.datetime.now()),
        data = getHumidityDataBase(sense_hat).__dict__
    )

# Pressure
def getPressureDataBase(sense_hat: SenseHat) -> DevicePressureDataBase:
            
    return DevicePressureDataBase(
        pressure = sense_hat.get_pressure(),
        temperature = sense_hat.get_temperature_from_pressure() 
    )

def getPressureData(sense_hat: SenseHat, session_id: uuid.UUID, datetime: datetime) -> DeviceDataBase:

    return DeviceDataBase(
        session_id = str(session_id),
        timestamp = str(datetime.datetime.now()),
        data = getPressureDataBase(sense_hat).__dict__
    )

#
# IMU data
# 

# Acceleration
def getAccelerometerDataBase(sense_hat: SenseHat) -> DeviceAccelerometerDataBase:
        
    accel = sense_hat.get_accelerometer()
    accelRaw = sense_hat.get_accelerometer_raw()

    return DeviceAccelerometerDataBase(
        roll = accel['roll'],
        pitch = accel['pitch'],
        yaw = accel['yaw'],
        x_raw = accelRaw['x'],
        y_raw = accelRaw['y'],
        z_raw = accelRaw['z']
    )

def getAccelerometerData(sense_hat: SenseHat, session_id: uuid.UUID, datetime: datetime) -> DeviceDataBase:
    
    return DeviceDataBase(
        session_id = str(session_id),
        timestamp = str(datetime.datetime.now()),
        data = getAccelerometerDataBase(sense_hat).__dict__
    )

# Gyroscope
def getGyroscopeDataBase(sense_hat: SenseHat) -> DeviceGyroscopeDataBase:
    
    gyro = sense_hat.get_gyroscope()
    gyroRaw = sense_hat.get_gyroscope_raw()

    return DeviceGyroscopeDataBase(
        roll = gyro['roll'],
        pitch = gyro['pitch'],
        yaw = gyro['yaw'],
        x_raw = gyroRaw['x'],
        y_raw = gyroRaw['y'],
        z_raw = gyroRaw['z']
    )

def getGyroscopeData(sense_hat: SenseHat, uuid: uuid.UUID, datetime: datetime) -> DeviceDataBase:
        
    return DeviceDataBase(
        session_id = str(uuid),
        timestamp = str(datetime.datetime.now()),
        data = getGyroscopeDataBase(sense_hat).__dict__
    )

# Magnetometer
def getMagnetometerDataBase(sense_hat: SenseHat) -> DeviceMagnetometerDataBase:
        
    compass = sense_hat.get_compass()
    compassRaw = sense_hat.get_compass_raw()

    return DeviceMagnetometerDataBase(
        north = compass,
        x_raw = compassRaw['x'],
        y_raw = compassRaw['y'],
        z_raw = compassRaw['z']
    )

def getMagnetometerData(sense_hat: SenseHat, uuid: uuid.UUID, datetime: datetime) -> DeviceDataBase:
        
    return DeviceDataBase(
        session_id = str(uuid),
        timestamp = str(datetime.datetime.now()),
        data = getMagnetometerDataBase(sense_hat).__dict__
    )

# Orientation
def getOrientationDataBase(sense_hat: SenseHat) -> DeviceOrientationDataBase:
        
    orientation = sense_hat.get_orientation_degrees()
    orientation_rad = sense_hat.get_orientation_radians()

    return DeviceOrientationDataBase(
        roll_deg = orientation['roll'],
        pitch_deg = orientation['pitch'],
        yaw_deg = orientation['yaw'],
        roll_rad = orientation_rad['roll'],
        pitch_rad = orientation_rad['pitch'],
        yaw_rad = orientation_rad['yaw']
    )

def getOrientationData(sense_hat: SenseHat, uuid: uuid.UUID, datetime: datetime) -> DeviceDataBase:
            
    return DeviceDataBase(
        session_id = str(uuid),
        timestamp = str(datetime.datetime.now()),
        data = getOrientationDataBase(sense_hat).__dict__
    )

#
# Pitch Roll data for Unity
#

# def getPitchRollData(sense_hat: SenseHat) -> DeviceOrientationPitchRollData:
            
#     orientation = sense_hat.get_orientation_degrees()

#     return DeviceOrientationPitchRollData(
#         roll = round(orientation['roll'], 1) ,
#         pitch = round(orientation['pitch'], 1)
#     )

def getPitchRollData(sense_hat: SenseHat) -> str:
            
    orientation = sense_hat.get_orientation_degrees()

    return f"{round(orientation['roll'], 1)} , {round(orientation['pitch'], 1)}"