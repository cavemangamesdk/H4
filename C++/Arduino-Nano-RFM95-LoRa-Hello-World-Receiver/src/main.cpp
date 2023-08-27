// RFM95 LoRa Hello World message receiver 

#include <Arduino.h>
#include <SPI.h>
#include <LoRa.h>

#define RFM95_CS 10
#define RFM95_RST 9
#define RFM95_INT 2

void setup() {
  Serial.begin(115200);
  while (!Serial);

  LoRa.setPins(RFM95_CS, RFM95_RST, RFM95_INT); // Set the NSS, RESET, and DIO0 pins

  if (!LoRa.begin(868E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }

  LoRa.setSpreadingFactor(7); // Set spreading factor (6-12)
  LoRa.setSignalBandwidth(125E3); // Set signal bandwidth (7.8E3, 10.4E3, 15.6E3, 20.8E3, 31.25E3, 41.7E3, 62.5E3, 125E3, 250E3, 500E3)
  LoRa.setCodingRate4(5); // Set coding rate (5-8)
  LoRa.setPreambleLength(8); // Set preamble length (default is 8)
  LoRa.setSyncWord(0x12); // Set sync word (default is 0x12)
  //LoRa.setTxPower(5);  // Set the transmit power to 17dBm
}

void loop() {

  // // Send a message
  // LoRa.beginPacket();
  // LoRa.print("Hello, LoRa!");
  // LoRa.endPacket();
  // //delay(2000);

  // Receive a message
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    while (LoRa.available()) {
      Serial.print((char)LoRa.read());
    }
    Serial.println();
  }
}