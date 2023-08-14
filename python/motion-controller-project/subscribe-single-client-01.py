import paho.mqtt.client as mqtt
#import Mqtt.paho_mqtt_helper as MqttHelper
import threading, time, keyboard, random

# Global flag variable to indicate when the threads should stop
running = True

# Init parameters
host = "3c6ea0ec32f6404db6fd0439b0d000ce.s2.eu.hivemq.cloud"
port = 8883
username = "mvp2023"
password = "wzq6h2hm%WLaMh$KYXj5"
client_id = ""
protocol = mqtt.MQTTv5
tls = mqtt.ssl.PROTOCOL_TLS

# 
topics = {
    "env":           "sensehat/env/#",
    "imu":           "sensehat/imu/#",
    "accelerometer": "sensehat/imu/accelerometer",
    "gyroscope":     "sensehat/imu/gyroscope",
    "magnetometer":  "sensehat/imu/magnetometer",
    "orientation":   "sensehat/imu/orientation",
    "humidity":      "sensehat/env/humidity",
    "pressure":      "sensehat/env/pressure"
}

# 
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Client " + str(client._client_id) + "Subscribed to: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    print("Message received: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_subscribe_callback(self):
    print(self)

#
def init_client(client_id, protocol, host, port, username, password, tls):
    client = mqtt.Client(client_id, userdata=None, protocol=protocol)
    if tls:
        client.tls_set(tls_version=tls)
    if username and password:
        client.username_pw_set(username, password)
    client.connect(host, port)

    return client

#
client = init_client(client_id, protocol, host, port, username, password, tls)

#
client.on_connect = on_connect
client.subscribe_callback = on_subscribe_callback
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

#
client.subscribe(topics["env"], qos=1) 

# For loop to subscribe to all topics
# for topic in topics:
#     client.subscribe(topics[topic], qos=1)

#
client.loop_forever()
