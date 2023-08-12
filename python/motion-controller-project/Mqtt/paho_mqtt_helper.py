import paho.mqtt.client as mqtt
import enum

from dataclasses import dataclass


# ENUMS

# MQTT protocol version
class MqttProtocol(enum.Enum):
    MQTTv31 = "MQTTv31"
    MQTTv311 = "MQTTv311"
    MQTTv5 = "MQTTv5"

# mqtt transport type
class MqttTransport(enum.Enum):
    TCP = "tcp"
    WEB_SOCKETS = "websockets"

# rc
class MqttRc(enum.Enum):
    CONNACK_ACCEPTED = 0
    CONNACK_REFUSED_PROTOCOL_VERSION = 1
    CONNACK_REFUSED_IDENTIFIER_REJECTED = 2
    CONNACK_REFUSED_SERVER_UNAVAILABLE = 3
    CONNACK_REFUSED_BAD_USERNAME_PASSWORD = 4
    CONNACK_REFUSED_NOT_AUTHORIZED = 5


# DATA_CLASSES

# Init MQTT client
@dataclass
class InitArgs:
    host: str
    port: int
    username: str
    password: str
    clientid: str
    protocol: MqttProtocol

# DICTS

# Init
initArgs = dict(
    host = "3c6ea0ec32f6404db6fd0439b0d000ce.s2.eu.hivemq.cloud",
    port = 8883,
    username = "mvp2023",
    password = "wzq6h2hm%WLaMh$KYXj5",
    clientid = "",
    protocol = MqttProtocol.MQTTv5
)

#
clientArgs = dict(
    client_id     = "", 
    clean_session = True, 
    userdata      = None, 
    protocol      = MqttProtocol.MQTTv5, 
    transport     = MqttTransport.TCP,
    reconnect_on_failure = True
)


# CALLBACKS

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

def on_subscribe_callback(self):
    print(self)


# HELPER FUNCTIONS

def initMqttClient(initArgs: InitArgs) -> bool:
    # Init MQTT client
    client = mqtt.Client(
        client_id     = initArgs.clientid, 
        clean_session = True, 
        userdata      = None, 
        protocol      = initArgs.protocol.value, 
        transport     = initArgs.transport.value,
        reconnect_on_failure = True
    )

    # enable TLS for secure connection
    client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
    # set username and password
    client.username_pw_set(initArgs.username, initArgs.password)
    # connect to HiveMQ Cloud on port 8883 (default for MQTT)
    client.connect(initArgs.host, initArgs.port)

    # setting callbacks, use separate functions like above for better visibility
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.on_publish = on_publish

    # subscribe to all topics of encyclopedia by using the wildcard "#"
    client.subscribe("encyclopedia/#", qos=1) 

    client.loop_forever()

    return True