from sense_hat import SenseHat
import get_data
import datetime
import uuid

#
sense = SenseHat()
uuidDevice = uuid.uuid4()
dateTime = datetime

# Test all get data functions
print(get_data.getAllDataBase(sense))
print(get_data.getAllData(sense, uuidDevice, dateTime))
print(get_data.getEnvDataBase(sense))
print(get_data.getEnvData(sense, uuidDevice, dateTime))
print(get_data.getHumidityDataBase(sense))
print(get_data.getHumidityData(sense, uuidDevice, dateTime))
print(get_data.getPressureDataBase(sense))
print(get_data.getPressureData(sense, uuidDevice, dateTime))
print(get_data.getImuDataBase(sense))
print(get_data.getImuData(sense, uuidDevice, dateTime))
print(get_data.getAccelerometerDataBase(sense))
print(get_data.getAccelerometerData(sense, uuidDevice, dateTime))
print(get_data.getGyroscopeDataBase(sense))
print(get_data.getGyroscopeData(sense, uuidDevice, dateTime))
print(get_data.getMagnetometerDataBase(sense))
print(get_data.getMagnetometerData(sense, uuidDevice, dateTime))
print(get_data.getOrientationDataBase(sense))
print(get_data.getOrientationData(sense, uuidDevice, dateTime))
