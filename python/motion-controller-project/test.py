from sense_hat import SenseHat
import get_data
import datetime
import uuid

# Sense Hat env data
sense = SenseHat()

# Disable and re-enable all IMU sensors in order to reset them
sense.set_imu_config(False, False, False)  # Disable all sensors
sense.set_imu_config(True, True, True)  # Enable all sensors

uuidDevice = uuid.uuid4()

dateTime = datetime

all_data = get_data.getAllData(sense, uuidDevice, dateTime) 

print(all_data)