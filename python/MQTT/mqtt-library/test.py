import pahoMqttHelper as mqtt
import random


print(mqtt.MqttRc.CONNACK_ACCEPTED.value)

broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt/foobar"
qos = 2
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

# Create client
client = mqtt.createClient(client_id)

# Set callback functions
mqtt.setCallbacks(client, mqtt.on_connect, mqtt.on_message, mqtt.on_publish, mqtt.on_subscribe)

# Connect to MQTT broker
result = mqtt.connect(client, broker, port)

print(f"Connected to broker: {result}")

mqtt.mqtt_client.loop_start()

# Publish a message
mqtt.publish(client, topic, "Hello World!")

# Subscribe to a topic
mqtt.subscribe(client, topic, qos)

mqtt.mqtt_client.loop_stop()

# Wait for publish
mqtt.mqtt_client.w

# Disconnect
mqtt.mqtt_client.disconnect()
