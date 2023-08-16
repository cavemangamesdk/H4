import time
import json
import random
import threading
import keyboard
import paho.mqtt.client as mqtt

# MQTT broker details
broker = "mqtt.eclipseprojects.io" #"mqtt.eclipse.org"
port = 1883

# Define the topic names
humidity_topic = "sensor/environment/humidity"
gyroscope_topic = "sensor/IMU/gyroscope"

# Raspberry Sense Hat sensor data collection logic
def collect_data():
    # Replace this with your actual sensor data collection logic
    humidity_data = random.uniform(0, 100)
    gyroscope_data = {
        "x": random.uniform(-1, 1),
        "y": random.uniform(-1, 1),
        "z": random.uniform(-1, 1)
    }
    return humidity_data, gyroscope_data

# MQTT publish function
def publish_data(topic, data):
    mqtt_client.publish(topic, json.dumps(data))

# Publish humidity data every minute
def publish_humidity_data():
    while True:
        humidity_data, _ = collect_data()
        publish_data(humidity_topic, humidity_data)
        time.sleep(60)

# Publish gyroscope data multiple times per second
def publish_gyroscope_data():
    while True:
        _, gyroscope_data = collect_data()
        publish_data(gyroscope_topic, gyroscope_data)
        time.sleep(0.1)

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))

# def on_publish(client, userdata, mid):
#     print("Message published")

def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# Create an MQTT client instance
mqtt_client = mqtt.Client()

# Enable debug mode / logging
mqtt_client.enable_logger()

# Set the MQTT client events
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish

# Connect to the MQTT broker
#mqtt_client.connect_async(broker, port, 60)
mqtt_client.connect_async("mqtt.eclipseprojects.io")

# Start the client loop in separate threads
mqtt_client.loop_start()

# Start the publishing threads
humidity_thread = threading.Thread(target=publish_humidity_data)
gyroscope_thread = threading.Thread(target=publish_gyroscope_data)

# Start the threads
humidity_thread.start()
gyroscope_thread.start()

# # Keep the main thread alive
# while True:
#     event = keyboard.read_key()
#     if event == 'a':  # Replace 'a' with the specific key you want to wait for
#         break
while True:
    if keyboard.is_pressed("esc"):
        break

# Stop the threadsa
mqtt_client.loop_stop()

# Disconnect from the MQTT broker
mqtt_client.disconnect()

# Exit the program
exit(0)