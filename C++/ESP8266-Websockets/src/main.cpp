#include <ESP8266WiFi.h>
#include <WebSocketsServer.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

// Replace with your network credentials
const char* ssid = "network 42";
const char* password = "12345678";

Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x29);

WebSocketsServer webSocket = WebSocketsServer(8765);

void webSocketEvent(uint8_t num, WStype_t type, uint8_t * payload, size_t length) {
  // Handle WebSocket event
}

void setup() {
  Serial.begin(115200);

  // Initialize BNO055 sensor
  if (!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while (1);
  }

  delay(1000);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println(WiFi.localIP());

  webSocket.begin();
  webSocket.onEvent(webSocketEvent);
}

void loop() {
  webSocket.loop();  // Handle WebSocket connections

  // Get orientation data from the BNO055 sensor
  sensors_event_t orientationData;
  bno.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);

  String x = String( orientationData.orientation.x);
  String y = String( orientationData.orientation.y);
  String z = String(-orientationData.orientation.z);

  // Convert the orientation data to a JSON string
  String message = y + ", " + x + ", " + z;

  // Send the JSON string to the WebSocket client
  webSocket.broadcastTXT(message);

  Serial.println(message);

  //delay(1000);  // Wait a second before getting the next sensor reading
}


