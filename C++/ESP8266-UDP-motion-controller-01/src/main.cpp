#include <ESP8266WiFiMulti.h>
#include <Adafruit_BNO055.h>
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

uint16_t UDP_PORT = 5100;

// Constants
const unsigned long serial_baudrate = 115200;

// Websocket server IP multicast
const IPAddress multicastIP(239, 1, 1, 1);
const uint16_t multicastPort = 5432;

// SSID & password of the Wi-Fi network you want to connect to (will connect to strongest)
const char* ssid0     = "dlink-C134";   
const char* password0 = "_BossPanda25"; 
// const char* ssid1     = "network 42";   
// const char* password1 = "12345678"; 
// const char* ssid2     = "4G Wi-Fi 3Danmark-1CBA";
// const char* password2 = "aircraft";
// const char* ssid3     = "Grundforlob";
// const char* password3 = "DataitGF";

//
Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x29);
ESP8266WiFiMulti wifiMulti;
WiFiUDP udp;

char* target_ip = "192.168.0.100";

// Functions
void ConnectBMO055() {
  Serial.println("Setting up orientation sensor...");
  if (!bno.begin()) {
    Serial.println("BNO055 not detected... Check wiring and I2C address!");
    while (1);
  }
  Serial.println("BNO055 detected!");
}

void ConnectWifi() {

  wifiMulti.addAP(ssid0, password0);
  // wifiMulti.addAP(ssid1, password1);
  // wifiMulti.addAP(ssid2, password2);
  // wifiMulti.addAP(ssid3, password3);

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

String ConnectMulticast() {
  Serial.println("Attempting to start UDP multicast listener...");
  if (udp.beginMulticast(WiFi.localIP(), multicastIP, multicastPort)) {
      Serial.println("UDP multicast listener started");
  } else {
    Serial.println("UDP multicast listener failed to start");
    exit(1);
  }

  while(udp.parsePacket() <= 0) {
    int packetSize = udp.parsePacket();
    if (packetSize) {
      char* sender_ip = (char*)udp.remoteIP().toString().c_str();
      Serial.println(sender_ip);
      Serial.println(packetSize);
      char incomingPacket[255];
      int len = udp.read(incomingPacket, 255);
      if (len > 0) {
        incomingPacket[len] = 0;
      }
      Serial.printf("UDP packet contents: %s\n", incomingPacket);
      //ws_ip = incomingPacket;
      //udp.stop();
      //udp.flush();+
      return String(incomingPacket);
    }
  }
  return String();
}

void GetOrientationData() {
  sensors_event_t orientationData;
  bno.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
  String oy = String(orientationData.orientation.y);
  String oz = String(-orientationData.orientation.z);
  String payload = oy + "," + oz;
  udp.beginPacket(target_ip, UDP_PORT);
  udp.write(payload.c_str());
  udp.endPacket();
}

void ConnectUdp(int port) {
  Serial.println("Seting up UDP client...");
  udp.begin(port);
  Serial.print("UDP server started on port ");
  Serial.println(port);
}

void setup() {
  Serial.begin(serial_baudrate);
  Serial.println("Setting up motion controller...");
  ConnectBMO055();
  ConnectWifi();
  //target_ip = (char*)ConnectMulticast().c_str();
  //Serial.println((char*)ConnectMulticast().c_str());
  ConnectUdp(UDP_PORT);
}

void loop() {
  GetOrientationData();
}