// https://tttapa.github.io/ESP8266/Chap07%20-%20Wi-Fi%20Connections.html

#include <Arduino.h>
#include <ESP8266WiFiMulti.h>   // Include the Wi-Fi-Multi library

ESP8266WiFiMulti wifiMulti;     // Create an instance of the ESP8266WiFiMulti class, called 'wifiMulti'

const char* ssid1     = "network 42";   // The SSID (name) of the Wi-Fi network you want to connect to
const char* password1 = "12345678";     // The password of the Wi-Fi network
const char* ssid2     = "4G Wi-Fi 3Danmark-1CBA";   // The SSID (name) of the Wi-Fi network you want to connect to
const char* password2 = "aircraft";     // The password of the Wi-Fi network
const char* ssid3     = "Grundforlob";   // The SSID (name) of the Wi-Fi network you want to connect to
const char* password3 = "DataitGF";     // The password of the Wi-Fi network

void ConnectMultipleWifi() {
  Serial.begin(115200);         // Start the Serial communication to send messages to the computer
  delay(10);
  Serial.println('\n');

  wifiMulti.addAP(ssid1, password1);   // add Wi-Fi networks you want to connect to
  wifiMulti.addAP(ssid2, password2);
  wifiMulti.addAP(ssid3, password3);

  Serial.println("Connecting ...");
  //int i = 0;
  while (wifiMulti.run() != WL_CONNECTED) { // Wait for the Wi-Fi to connect: scan for Wi-Fi networks, and connect to the strongest of the networks above
    delay(1000);
    Serial.print('.');
  }
  Serial.println('\n');
  Serial.print("Connected to ");
  Serial.println(WiFi.SSID());              // Tell us what network we're connected to
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());           // Send the IP address of the ESP8266 to the computer
}

void setup() { 
  ConnectMultipleWifi();
}

void loop() { 
}