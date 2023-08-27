/*
    Motion controller based on the ESP8266 and the BNO055 sensor
*/

// Includes
#include <ESP8266WiFiMulti.h>
#include <Adafruit_BNO055.h>
#include <WebSocketsClient.h>

// Constants
const unsigned long serial_baudrate = 115200;

// SSID & password of the Wi-Fi network you want to connect to (will connect to strongest)
const char* ssid1     = "network 42";   
const char* password1 = "12345678"; 
const char* ssid2     = "4G Wi-Fi 3Danmark-1CBA";
const char* password2 = "aircraft";
const char* ssid3     = "Grundforlob";
const char* password3 = "DataitGF";

// Websocket server
const char* ws_ip = "192.168.8.104";
//const char* ws_ip = "192.168.5.113";
const uint16_t ws_port = 80;
const char* ws_path = "/MotionController";

//
Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x29);
ESP8266WiFiMulti wifiMulti;
WebSocketsClient webSocket;

// Functions
void ConnectBMO055() {
  if (!bno.begin()) {
    Serial.print("BNO055 not detected... Check wiring and I2C address!");
    while (1);
  }
  Serial.print("BNO055 detected!");
}

void ConnectWifi() {

  wifiMulti.addAP(ssid1, password1);
  wifiMulti.addAP(ssid2, password2);
  wifiMulti.addAP(ssid3, password3);

  Serial.println("Connecting Wifi");
  
  while (wifiMulti.run() != WL_CONNECTED) {
    delay(100);
    Serial.print('.');
  }
  Serial.println('\n');
  Serial.print("Connected to ");
  Serial.println(WiFi.SSID());
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());
}

void webSocketEvent(WStype_t type, uint8_t * payload, size_t length) {
  // Boilerplate websocket event handler
  switch(type) {
    case WStype_DISCONNECTED:
      Serial.printf("[WSc] Disconnected!\n");
      break;
    case WStype_CONNECTED:
      Serial.printf("[WSc] Connected to url: %s\n", payload);
      break;
    case WStype_TEXT:
      Serial.printf("[WSc] get text: %s\n", payload);
      break;
    case WStype_BIN:
      Serial.printf("[WSc] get binary length: %u\n", length);
      break;
    case WStype_PING:
      Serial.printf("[WSc] get ping\n");
      break;
    case WStype_PONG:
      Serial.printf("[WSc] get pong\n");
      break;
    case WStype_ERROR:
      Serial.printf("[WSc] get error\n");
      break;
    case WStype_FRAGMENT_TEXT_START:
      Serial.printf("[WSc] get fragment text start\n");
      break;
    case WStype_FRAGMENT_BIN_START:
      Serial.printf("[WSc] get fragment bin start\n");
      break;
    case WStype_FRAGMENT:
      Serial.printf("[WSc] get fragment\n");
      break;
    case WStype_FRAGMENT_FIN:
      Serial.printf("[WSc] get fragment fin\n");
      break;
  }
}

void ConnectWebSocket() {
  webSocket.begin(ws_ip, ws_port, ws_path);
  webSocket.onEvent(webSocketEvent);
  webSocket.setReconnectInterval(1000);
  webSocket.enableHeartbeat(15000, 3000, 2);
}

void GetOrientationData() {
  sensors_event_t orientationData;
  bno.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
  String oy = String( orientationData.orientation.y);
  String oz = String(-orientationData.orientation.z);
  String payload = oy + "," + oz;
  webSocket.sendTXT(payload);
  //Serial.println(message);
}

void setup() {
  Serial.begin(serial_baudrate);
  ConnectBMO055();
  ConnectWifi();
  ConnectWebSocket();
}

void loop() {
  webSocket.loop();
  GetOrientationData();
}