from sense_hat import SenseHat
import time
import datetime
import json

import paho.mqtt.client as paho
from paho import mqtt

import DeviceEnvironmentData as envData

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


while True:

    # Get sensor data
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    # Create DeviceEnvironmentData object
    #data = envData.DeviceEnvironmentData(str(datetime.datetime.now()), 42.0, 42.0, 42.0)
    data = envData.DeviceEnvironmentData(str(datetime.datetime.now()), temperature, humidity, pressure)

    # Convert to JSON
    dataJson = json.dumps(data.__dict__)

    # Send over MQTT
    client.loop_start()
    client.publish("encyclopedia/environment", payload=dataJson, qos=1)
    client.loop_stop()
     
    time.sleep(1)