import paho.mqtt.client as mqtt
import threading, time, keyboard, random
from typing import Callable, Any
import get_data as data

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
    "temperature":   "sensehat/env/temperature",
    "humidity":      "sensehat/env/humidity",
    "pressure":      "sensehat/env/pressure"
}

# 
clients = []
threads = []

# Callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))

def on_publish(client, userdata, mid):
    print("Message published")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.topic} {str(msg.payload)}")


#
def publish_data(client: mqtt.Client, topic: str, data: Callable[[Any], Any], interval: float):
    client.publish(topic, data)
    time.sleep(interval)

# Create new client
def create_client(client_id: str, username: str, password: str, protocol: mqtt.MQTTv5, tls: mqtt.ssl.PROTOCOL_TLS) -> mqtt.Client:
    client = mqtt.Client(client_id=client_id, protocol=protocol)
    client.username_pw_set(username=username, password=password)
    client.tls_set(tls)
    clients.append(client)
    return client

def create_thread(target, args) -> threading.Thread:
    thread = threading.Thread(target=target, args=args)
    threads.append(thread)
    return thread

# Create MQTT clients for each topic, with a unique client_id
client1 = create_client(client_id="environment", username=username, password=password, protocol=protocol, tls=tls)

client1.on_connect = on_connect
client1.on_publish = on_publish

# Connect asynchronously to the MQTT broker
client1.connect_async(host=host, port=port)

# Start the client loop in a separate thread
client1.loop_start()

# Create threads
temperature_thread = create_thread(target=publish_data, args=(client1, topics["env"], data.getAllData(), 5.0))

temperature_thread.start()

# Stop the MQTT client loops
client1.loop_stop()

# Disconnect from the MQTT broker
client1.disconnect()

# Exit the program
exit(0)