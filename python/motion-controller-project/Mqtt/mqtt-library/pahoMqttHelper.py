from paho.mqtt import client as mqtt_client
from typing import Callable, Any
import enum

# mqtt protocol enum
class MqttProtocol(enum.Enum):
    MQTTv31 = "MQTTv31"
    MQTTv311 = "MQTTv311"
    MQTTv5 = "MQTTv5"

# mqtt transport enum
class MqttTransport(enum.Enum):
    TCP = "tcp"
    WEB_SOCKETS = "websockets"

# rc enum 
class MqttRc(enum.Enum):
    CONNACK_ACCEPTED = 0
    CONNACK_REFUSED_PROTOCOL_VERSION = 1
    CONNACK_REFUSED_IDENTIFIER_REJECTED = 2
    CONNACK_REFUSED_SERVER_UNAVAILABLE = 3
    CONNACK_REFUSED_BAD_USERNAME_PASSWORD = 4
    CONNACK_REFUSED_NOT_AUTHORIZED = 5

#
clientArgs = dict(
    client_id     = "", 
    clean_session = True, 
    userdata      = None, 
    protocol      = mqtt_client.MQTTv5, 
    transport     = MqttTransport.TCP,
    reconnect_on_failure = True
)


# Callback functions
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
def connect(client: mqtt_client, broker: str, port: int) -> bool:
    return client.connect(broker, port)

# Connect async
def connectAsync(client: mqtt_client, broker: str, port: int) -> bool:
    return client.connect_async(broker, port)

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
