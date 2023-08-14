from sense_hat import SenseHat
import get_data
import datetime
import uuid

#
sense = SenseHat()
uuidDevice = uuid.uuid4()
dateTime = datetime

# Test all get data functions
#data = get_data.getAllDataBase(sense)
#data = get_data.getAllData(sense, uuidDevice, dateTime)
data = get_data.getEnvDataBase(sense)
#data = get_data.getEnvData(sense, uuidDevice, dateTime)
#data = get_data.getHumidityDataBase(sense)
#data = get_data.getHumidityData(sense, uuidDevice, dateTime)
#data = get_data.getPressureDataBase(sense)
#data = get_data.getPressureData(sense, uuidDevice, dateTime)
#data = get_data.getImuDataBase(sense)
#data = get_data.getImuData(sense, uuidDevice, dateTime)
#data = get_data.getAccelerationDataBase(sense)
#data = get_data.getAccelerationData(sense, uuidDevice, dateTime)
#data = get_data.getGyroscopeDataBase(sense)
#data = get_data.getGyroscopeData(sense, uuidDevice, dateTime)
#data = get_data.getMagnetometerDataBase(sense)
#data = get_data.getMagnetometerData(sense, uuidDevice, dateTime)
#data = get_data.getOrientationDataBase(sense)
#data = get_data.getOrientationData(sense, uuidDevice, dateTime)

print(data)