// https://tttapa.github.io/ESP8266/Chap07%20-%20Wi-Fi%20Connections.html

#include <Arduino.h>
#include <ESP8266WiFi.h>        // Include the Wi-Fi library

const char* ssid1     = "network 42";   // The SSID (name) of the Wi-Fi network you want to connect to
const char* password1 = "12345678";     // The password of the Wi-Fi network

void ConnectSingleWifi() {
  Serial.begin(115200);         // Start the Serial communication to send messages to the computer
  delay(10);
  Serial.println('\n');
  
  WiFi.begin(ssid1, password1);             // Connect to the network
  Serial.print("Connecting to ");
  Serial.print(ssid1); Serial.println(" ...");

  int i = 0;
  while (WiFi.status() != WL_CONNECTED) { // Wait for the Wi-Fi to connect
    delay(1000);
    Serial.print(++i); Serial.print(' ');
  }

  Serial.println('\n');
  Serial.println("Connection established!");  
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());         // Send the IP address of the ESP8266 to the computer
}

void setup() { 
  ConnectSingleWifi();
}

void loop() { 
  
}