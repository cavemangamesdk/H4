import paho_mqtt_helper as mqtt

initArgs = mqtt.InitArgs(
    host = "3c6ea0ec32f6404db6fd0439b0d000ce.s2.eu.hivemq.cloud",
    port = 8883,
    username = "mvp2023",
    password = "wzq6h2hm%WLaMh$KYXj5",
    clientid = "",
    protocol = mqtt.MqttProtocol.MQTTv5
)

mqtt.initMqttClient(initArgs)

