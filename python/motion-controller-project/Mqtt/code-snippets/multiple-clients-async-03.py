import paho.mqtt.client as mqtt
import threading
import time
import keyboard

# Global flag variable to indicate when the threads should stop
running = True

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))

def on_publish(client, userdata, mid):
    print("Message published")

def publish_temperature(client):
    while running:
        client.publish("sensor/temperature", "25")
        time.sleep(2)  # Publish every 2 seconds

def publish_gyroscope(client):
    while running:
        client.publish("sensor/gyroscope", "0.5")
        time.sleep(0.1)  # Publish every 0.1 seconds

# Create MQTT clients for each topic
client1 = mqtt.Client()
client2 = mqtt.Client()

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

while True:
    if keyboard.is_pressed("esc"):
        #break

        # Wait for the threads to finish
        temperature_thread.join()
        gyroscope_thread.join()

        # Stop the MQTT client loops
        client1.loop_stop()
        client2.loop_stop()

        # Disconnect from the MQTT broker
        client1.disconnect()
        client2.disconnect()

        # Exit the program
        exit(0)
