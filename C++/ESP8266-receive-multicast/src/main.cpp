#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

const IPAddress multicastIP(224, 1, 1, 1);
const int multicastPort = 4567;

const char* ssid = "4G Wi-Fi 3Danmark-1CBA";
const char* password = "aircraft";

WiFiUDP udp;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.println(WiFi.localIP());

  if (udp.beginMulticast(WiFi.localIP(), multicastIP, multicastPort)) {
    Serial.println("UDP multicast listener started");
  } else {
    Serial.println("UDP multicast listener failed to start");
  }
}

void loop() {
  int packetSize = udp.parsePacket();
  if (packetSize) {
    char incomingPacket[255];
    int len = udp.read(incomingPacket, 255);
    if (len > 0) {
      incomingPacket[len] = 0;
    }
    Serial.printf("UDP packet contents: %s\n", incomingPacket);
  }
}




// #include <ESP8266WiFi.h>
// #include <WiFiUdp.h>

// const char* ssid = "4G Wi-Fi 3Danmark-1CBA";
// const char* password = "aircraft";

// WiFiUDP Udp;
// unsigned int localUdpPort = 5007;  // local port to listen on

// char incomingPacket[255];  // buffer for incoming packets
// char  replyPacket[] = "Hi there! Got the message :-)";  // a reply string to send back

// void setup()
// {
//     Serial.begin(115200);
//     Serial.println();

//     Serial.printf("Connecting to %s ", ssid);
//     WiFi.begin(ssid, password);
//     while (WiFi.status() != WL_CONNECTED)
//     {
//         delay(500);
//         Serial.print(".");
//     }
//     Serial.println(" connected");

//     Udp.begin(localUdpPort);
//     Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUdpPort);
// }

// void loop()
// {
//     int packetSize = Udp.parsePacket();
//     if (packetSize)
//     {
//         // receive incoming UDP packets
//         Serial.printf("Received %d bytes from %s, port %d\n", packetSize, Udp.remoteIP().toString().c_str(), Udp.remotePort());
//         int len = Udp.read(incomingPacket, 255);
//         if (len > 0)
//         {
//             incomingPacket[len] = 0;
//         }
//         Serial.printf("UDP packet contents: %s\n", incomingPacket);

//         // send back a reply, to the IP address and port we got the packet from
//         Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
//         Udp.write(replyPacket);
//         Udp.endPacket();
//     }
// }



// #include <ESP8266WiFi.h>
// #include <WiFiUdp.h>

// const char* ssid = "4G Wi-Fi 3Danmark-1CBA";
// const char* password = "aircraft";

// WiFiUDP Udp;
// unsigned int multicastPort = 58008;  // local port to listen on
// IPAddress multicastIP(224,1,1,1);

// void setup(){
//     Serial.begin(115200);
//     Serial.println();

//     Serial.printf("Connecting to %s ", ssid);
//     WiFi.begin(ssid, password);
//     while (WiFi.status() != WL_CONNECTED)
//     {
//     delay(500);
//     Serial.print(".");
//     }
//     Serial.println("connected");
    
//     //Udp.begin(multicastPort);
//     Udp.beginMulticast(WiFi.localIP(), multicastIP, multicastPort);
//     Serial.printf("Now listening at IP %s and %s, UDP port %d\n", WiFi.localIP().toString().c_str(), multicastIP.toString().c_str(), multicastPort);
// }


// void loop(){
//     int packetSize = Udp.parsePacket();
//     if (packetSize){
//     Serial.println("RECEIVED!");
//     }
// }