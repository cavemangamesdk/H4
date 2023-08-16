import paho.mqtt.client as mqtt
import threading
import time
import keyboard

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))

# def on_publish(client, userdata, mid):
#     print("Message published")

def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

def publish_temperature(client):
    while True:
        client.publish("sensor/temperature", "25")
        time.sleep(2)  # Publish every minute

def publish_gyroscope(client):
    while True:
        client.publish("sensor/gyroscope", "0.5")
        time.sleep(0.1)  # Publish as often as possible


# Create MQTT clients for each topic
client1 = mqtt.Client()
client2 = mqtt.Client()

# Enable debug mode / logging
client1.enable_logger()
client2.enable_logger()

# Set up the on_connect and on_publish callbacks
client1.on_connect = on_connect
client1.on_publish = on_publish
client2.on_connect = on_connect
client2.on_publish = on_publish

# Connect asynchronously to the MQTT broker
client1.connect_async("mqtt.eclipseprojects.io")
client2.connect_async("mqtt.eclipseprojects.io")

# Start the client loops in separate threads
client1.loop_start()
client2.loop_start()

# Create threads for publishing at different intervals
temperature_thread = threading.Thread(target=publish_temperature, args=(client1,))
gyroscope_thread = threading.Thread(target=publish_gyroscope, args=(client2,))

# Start the publishing threads
temperature_thread.start()
gyroscope_thread.start()

# While loop that keeps the main thread alive until escape key is pressed
while True:
    if keyboard.is_pressed("esc"):
        break


# Stop the threads
client1.loop_stop()
client2.loop_stop()

# Disconnect from the MQTT broker
client1.disconnect()
client2.disconnect()

# Exit the program
exit(0)