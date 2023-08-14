from sense_hat import SenseHat
import get_data
import datetime
import uuid

#
sense = SenseHat()
uuidDevice = uuid.uuid4()
dateTime = datetime

# Test all get data functions
print(get_data.getAllDataBase(sense).__dict__)
print(get_data.getAllData(sense, uuidDevice, dateTime).__dict__)
print(get_data.getEnvDataBase(sense).__dict__)
print(get_data.getEnvData(sense, uuidDevice, dateTime).__dict__)
print(get_data.getHumidityDataBase(sense).__dict__)
print(get_data.getHumidityData(sense, uuidDevice, dateTime).__dict__)
print(get_data.getPressureDataBase(sense).__dict__)
print(get_data.getPressureData(sense, uuidDevice, dateTime).__dict__)
print(get_data.getImuDataBase(sense).__dict__)
print(get_data.getImuData(sense, uuidDevice, dateTime).__dict__)
print(get_data.getAccelerometerDataBase(sense).__dict__)
print(get_data.getAccelerometerData(sense, uuidDevice, dateTime).__dict__)
print(get_data.getGyroscopeDataBase(sense).__dict__)
print(get_data.getGyroscopeData(sense, uuidDevice, dateTime).__dict__)
print(get_data.getMagnetometerDataBase(sense).__dict__)
print(get_data.getMagnetometerData(sense, uuidDevice, dateTime).__dict__)
print(get_data.getOrientationDataBase(sense).__dict__)
print(get_data.getOrientationData(sense, uuidDevice, dateTime).__dict__)
