import paho.mqtt.client as mqtt
import threading
import time
import keyboard

# Global flag variable to indicate when the threads should stop
running = True

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))

def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT broker with result code " + str(rc))

def on_publish(client, userdata, mid):
    print("Message published")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to topic!")

def on_message(client, userdata, msg):
    print("Message received: " + msg.topic + " " + str(msg.payload.decode()))

def publish_temperature(client):
    while running:
        client.publish("$SYS/temperature", "25")
        time.sleep(2)  # Publish every 2 seconds

def publish_gyroscope(client):
    while running:
        client.publish("$SYS/gyroscope", "0.5")
        time.sleep(0.1)  # Publish every 0.1 seconds

def stop_program(_=None):
    global running
    running = False

    # # Wait for the threads to finish
    # temperature_thread.join()
    # gyroscope_thread.join()

    # # Stop the MQTT client loops
    # client1.loop_stop()
    # client2.loop_stop()
    # client3.loop_stop()
    # print("loops stopped!")

    # # Disconnect from the MQTT broker
    # client1.disconnect()
    # client2.disconnect()
    # client3.disconnect()
    # print("disconnected!")

    # Exit the program
    #exit(0)

# Create MQTT clients for each topic
client1 = mqtt.Client()
client2 = mqtt.Client()
client3 = mqtt.Client()

# Set up the on_connect and on_publish callbacks
client1.on_connect = on_connect
client1.on_disconnect = on_disconnect
client1.on_publish = on_publish

client2.on_connect = on_connect
client2.on_disconnect = on_disconnect
client2.on_publish = on_publish

client3.on_connect = on_connect
client3.on_disconnect = on_disconnect
client3.on_subscribe = on_subscribe
client3.on_message = on_message

# Connect asynchronously to the MQTT broker
client1.connect_async("mqtt.eclipseprojects.io")
client2.connect_async("mqtt.eclipseprojects.io")
client3.connect_async("mqtt.eclipseprojects.io")

# Subscribe to the topic
client3.subscribe("sensor/#")

# Start the client loops in separate threads
client1.loop_start()
client2.loop_start()
client3.loop_start()

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
client3.loop_stop()

# Disconnect from the MQTT broker
client1.disconnect()
client2.disconnect()
client3.disconnect()

# Exit the program
exit(0)
