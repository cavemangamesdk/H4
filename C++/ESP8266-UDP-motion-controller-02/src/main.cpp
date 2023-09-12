#include <ESP8266WiFiMulti.h>
#include <Adafruit_BNO055.h>
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

// Constants
const unsigned long serial_baudrate = 115200;

// SSID & password of the Wi-Fi network you want to connect to (will connect to strongest)
const char* ssid0     = "network 42";   
const char* password0 = "12345678"; 

// Target IPv4 address and port the UDP client will connect to
char* target_ip = "192.168.109.1";
uint16_t udp_port = 5100;

//
Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x29);
ESP8266WiFiMulti wifiMulti;
WiFiUDP udp;

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

void GetOrientationData() {
  sensors_event_t orientationData;
  bno.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
  String oy = String(orientationData.orientation.y);
  String oz = String(-orientationData.orientation.z);
  String payload = oy + "," + oz;
  udp.beginPacket(target_ip, udp_port);
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
  ConnectUdp(udp_port);
}

void loop() {
  GetOrientationData();
}