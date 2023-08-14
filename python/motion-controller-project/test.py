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

print(data)