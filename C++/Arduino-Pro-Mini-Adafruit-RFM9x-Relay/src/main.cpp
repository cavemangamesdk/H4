// Arduino Pro Mini + RFM95 LoRa relay. Transmits back whatever it receives.

#include <Arduino.h>
#include <SPI.h>
#include <LoRa.h>

#define RFM95_CS 4
#define RFM95_RST 2
#define RFM95_INT 3

// const int csPin = 4;          // LoRa radio chip select
// const int resetPin = 2;        // LoRa radio reset
// const int irqPin = 3;          // change for your board; must be a hardware interrupt pin

String receivedData = "";

void receiveData() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    // received a packet
    Serial.print("Received packet '");
    while (LoRa.available()) {
      receivedData = LoRa.readString();
      Serial.print(receivedData);
    }
    // print RSSI of packet
    Serial.print("' with RSSI ");
    Serial.println(LoRa.packetRssi());
  }
}

void sendData() {
  // send packet
  Serial.println("Sending packet...");
  LoRa.beginPacket();
  LoRa.print(receivedData);
  LoRa.endPacket();
  receivedData = "";  // Clear received data
}

void setup() {
  Serial.begin(115200);
  while (!Serial);
  Serial.println("LoRa Relay setup...");

  LoRa.setPins(RFM95_CS, RFM95_RST, RFM95_INT); // Set the NSS, RESET, and DIO0 pins

  if (!LoRa.begin(433E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }

  LoRa.setSpreadingFactor(7); // Set spreading factor (6-12)
  LoRa.setSignalBandwidth(125E3); // Set signal bandwidth (7.8E3, 10.4E3, 15.6E3, 20.8E3, 31.25E3, 41.7E3, 62.5E3, 125E3, 250E3, 500E3)
  LoRa.setCodingRate4(5); // Set coding rate (5-8)
  LoRa.setPreambleLength(8); // Set preamble length (default is 8)
  LoRa.setSyncWord(0x12); // Set sync word (default is 0x12)
  LoRa.setTxPower(17);  // Set the transmit power (2-20, default is 17 dBm)

  Serial.println("LoRa Initializing OK!");
}

void loop() {
  receiveData();
  if (receivedData != "") {
    delay(100);  // Delay for 1 second
    sendData();
  }
}