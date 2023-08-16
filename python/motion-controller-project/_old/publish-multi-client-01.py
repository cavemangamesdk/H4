import paho.mqtt.client as mqtt
import threading, time, keyboard, random

# Global flag variable to indicate when the threads should stop
running = True

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    # Subscribe to all relevant topics
    client.subscribe("sensor/temperature")
    client.subscribe("sensor/gyroscope")

def on_publish(client, userdata, mid):
    print("Message published")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.topic} {str(msg.payload)}")

def publish_temperature(client):
    while running:
        client.publish("sensor/temperature", str(random.uniform(15, 25)))
        time.sleep(2)  # Publish every 2 seconds

def publish_gyroscope(client):
    while running:
        client.publish("sensor/gyroscope", str(random.uniform(-1.0, 1.0)))
        time.sleep(0.1)  # Publish every 0.1 seconds

def stop_program(_=None):
    global running
    running = False

# Create MQTT clients for each topic
client1 = mqtt.Client()
client2 = mqtt.Client()
client3 = mqtt.Client()  # Client for subscribing to topics

# Set up the on_connect and on_publish callbacks
client1.on_connect = on_connect
client1.on_publish = on_publish
client2.on_connect = on_connect
client2.on_publish = on_publish
client3.on_connect = on_connect
client3.on_message = on_message  # Set up the on_message callback for the subscribing client

# Connect asynchronously to the MQTT broker
client1.connect_async("mqtt.eclipseprojects.io")
client2.connect_async("mqtt.eclipseprojects.io")
client3.connect_async("mqtt.eclipseprojects.io")

# Start the client loops in separate threads
client1.loop_start()
client2.loop_start()
client3.loop_start()  # Start the loop for the subscribing client

# Create threads for publishing at different intervals
temperature_thread = threading.Thread(target=publish_temperature, args=(client1,))
gyroscope_thread = threading.Thread(target=publish_gyroscope, args=(client2,))

# Start the publishing threads
temperature_thread.start()
gyroscope_thread.start()

# Register the escape key press event handler
keyboard.on_press_key("esc", stop_program)

# Wait for the threads to finish
temperature_thread.join()
gyroscope_thread.join()

# Stop the MQTT client loops
client1.loop_stop()
client2.loop_stop()
client3.loop_stop()  # Stop the loop for the subscribing client

# Disconnect from the MQTT broker
client1.disconnect()
client2.disconnect()
client3.disconnect()  # Disconnect the subscribing client

# Exit the program
exit(0)
