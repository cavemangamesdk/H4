from sense_hat import SenseHat
import time
import datetime
import json
import uuid

import paho.mqtt.client as paho
from paho import mqtt

import GetData as getData

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_subscribe_callback(self):
    print(self)

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect
client.subscribe_callback = on_subscribe_callback

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("mvp2023", "wzq6h2hm%WLaMh$KYXj5")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("3c6ea0ec32f6404db6fd0439b0d000ce.s2.eu.hivemq.cloud", 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("encyclopedia/#", qos=1) 

# Sense Hat env data
sense = SenseHat()

# Disable and re-enable all IMU sensors in order to reset them
sense.set_imu_config(False, False, False)  # Disable all sensors
sense.set_imu_config(True, True, True)  # Enable all sensors

uuidDevice = uuid.uuid4()

dateTime = datetime

while True:

    # Get sensor data
    allData = getData.getAllData(sense, uuidDevice, dateTime)
    # accelerationData = getData.getAccelerometerData(sense, uuidDevice, dateTime)
    # environmentData = getData.getEnvironmentData(sense, uuidDevice, dateTime)
    # gyroscopeData = getData.getGyroscopeData(sense, uuidDevice, dateTime)
    # magnetometerData = getData.getMagnetometerData(sense, uuidDevice, dateTime)
    # orientationData = getData.getOrientationData(sense, uuidDevice, dateTime)

    # Send over MQTT
    client.loop_start()
    client.publish(topic="encyclopedia/all", payload=json.dumps(allData.__dict__), qos=2)
    # client.publish(topic="encyclopedia/acceleration", payload=json.dumps(accelerationData.__dict__), qos=2)
    # client.publish(topic="encyclopedia/environment", payload=json.dumps(environmentData.__dict__), qos=2)
    # client.publish(topic="encyclopedia/gyroscope", payload=json.dumps(gyroscopeData.__dict__), qos=2)
    # client.publish(topic="encyclopedia/magnetometer", payload=json.dumps(magnetometerData.__dict__), qos=2)
    # client.publish(topic="encyclopedia/orientation", payload=json.dumps(orientationData.__dict__), qos=2)
    client.loop_stop()
     
    time.sleep(1)