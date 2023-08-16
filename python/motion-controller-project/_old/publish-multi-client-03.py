import paho.mqtt.client as mqtt
import threading, time, keyboard, random, datetime, json, uuid
import paho.mqtt.client as paho
import get_data as getData
from sense_hat import SenseHat
from typing import Callable, Any

host = "3c6ea0ec32f6404db6fd0439b0d000ce.s2.eu.hivemq.cloud"
port = 8883
username = "mvp2023"
password = "wzq6h2hm%WLaMh$KYXj5"
client_id = ""
protocol = mqtt.MQTTv5
tls = mqtt.ssl.PROTOCOL_TLS

# Global flag variable to indicate when the threads should stop
running = True

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

def on_publish(client, userdata, mid):
    print("Message published")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.topic} {str(msg.payload)}")

#
def publish(client: mqtt.Client, topic: str, interval: float, function: Callable[[Any], Any], sense, uuidDevice, dateTime):
    while running:
        data = json.dumps(function(sense, uuidDevice, dateTime).__dict__)
        client.publish(topic=topic, payload=data, qos=2)
        time.sleep(interval)

def stop_program(_=None):
    global running
    running = False


#
sense = SenseHat()
uuidDevice = uuid.uuid4()
dateTime = datetime

#
client1 = mqtt.Client(client_id="1", protocol=protocol)
client1.username_pw_set(username=username, password=password)
client1.tls_set(tls_version=tls)


# Set up the on_connect and on_publish callbacks
client1.on_connect = on_connect
client1.on_publish = on_publish

# Connect asynchronously to the MQTT broker
client1.connect_async(host=host, port=port)

#client3.subscribe("sensehat/#")  # Subscribe to all topics under sensehat

# Start the client loops in separate threads
client1.loop_start()

# Create threads for publishing at different intervals
gyroscope_thread = threading.Thread(target=publish, args=(client1, "sensehat/imu/gyroscope", 1.0, getData.getGyroscopeData, sense, uuidDevice, dateTime))

# Start the publishing threads
#temperature_thread.start()
gyroscope_thread.start()

# Register the escape key press event handler
keyboard.on_press_key("esc", stop_program)

# Wait for the threads to finish
#temperature_thread.join()
gyroscope_thread.join()

# Stop the MQTT client loops
client1.loop_stop()

# Disconnect from the MQTT broker
client1.disconnect()

# Exit the program
exit(0)
