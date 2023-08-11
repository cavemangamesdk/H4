from paho.mqtt import client as mqtt_client
from typing import Callable, Any

# Callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

def on_publish(client, userdata, mid):
    print(f"Published message with id `{mid}`")

def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Subscribed to `{mid}` with QoS `{granted_qos}`")

# Create client
def createClient(clientId: int) -> mqtt_client:
    return mqtt_client.Client(clientId)

# Set callback functions
def setCallbacks(client: mqtt_client, on_connect: Callable[[Any, Any, Any, Any], None], on_message: Callable[[Any, Any, Any], None], on_publish: Callable[[Any, Any, int], None], on_subscribe: Callable[[Any, Any, int, int], None]):
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    client.on_subscribe = on_subscribe

# Connect to MQTT broker
def connect(client: mqtt_client, broker: str, port: int):
    client.connect(broker, port)

# Publish a message
def publish(client: mqtt_client, topic: str, message: str):
    result = client.publish(topic, message)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{message}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

# Subscribe to a topic
def subscribe(client: mqtt_client, topic: str, qos: int = 0):
    client.subscribe(topic, qos)

# Run the client
def run(client: mqtt_client):
    client.loop_forever()
