import mqtt as mqtt
import random

broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt/foobar"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

# Create client
client = mqtt.createClient(client_id)

# Set callback functions
mqtt.setCallbacks(client, mqtt.on_connect, mqtt.on_message, mqtt.on_publish, mqtt.on_subscribe)

# Connect to MQTT broker
mqtt.connect(client, broker, port)

# Publish a message
mqtt.publish(client, topic, "Hello World!")

# Subscribe to a topic
mqtt.subscribe(client, topic)

# Run the client
mqtt.run(client)

