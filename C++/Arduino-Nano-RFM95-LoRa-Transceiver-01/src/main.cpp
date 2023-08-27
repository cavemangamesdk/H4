// Arduino Nano (new bootloader) + RFM95 LoRa transceiver.

#include <Arduino.h>
#include <SPI.h>
#include <LoRa.h>

#define RFM95_NSS 10
#define RFM95_RST  9
#define RFM95_DIO0 2

unsigned long previousMillis = 0; 
const long interval = 2000;  // interval to send data (2 seconds)

void receiveData() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    // received a packet
    Serial.print("Received packet '");
    while (LoRa.available()) {
      String LoRaData = LoRa.readString();
      Serial.print(LoRaData);
    }
    // print RSSI of packet
    Serial.print("' with RSSI ");
    Serial.println(LoRa.packetRssi());
  }
}

void sendData() {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    // send packet
    Serial.println("Sending packet...");
    LoRa.beginPacket();
    LoRa.print("Hello ");
    LoRa.endPacket();
  }
}

void setup() {
  Serial.begin(115200);
  while (!Serial);
  Serial.println("LoRa Transceiver setup...");

  LoRa.setPins(RFM95_NSS, RFM95_RST, RFM95_DIO0); // Set the NSS, RESET, and DIO0 pins

  if (!LoRa.begin(868E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }

  LoRa.setSpreadingFactor(7); // Set spreading factor (6-12)
  LoRa.setSignalBandwidth(125E3); // Set signal bandwidth (7.8E3, 10.4E3, 15.6E3, 20.8E3, 31.25E3, 41.7E3, 62.5E3, 125E3, 250E3, 500E3)
  LoRa.setCodingRate4(5); // Set coding rate (5-8)
  LoRa.setPreambleLength(8); // Set preamble length (6-65535, default is 8)
  LoRa.setSyncWord(0x12); // Set sync word (default is 0x12)
  LoRa.setTxPower(2);  // Set the transmit power (2-20, default is 17 dBm)

  Serial.println("LoRa Initializing OK!");
}

void loop() {
  sendData();
  receiveData();
}