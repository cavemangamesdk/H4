#include "WiFi.h"
#include "SPIFFS.h"
#include "ESPAsyncWebServer.h"
 
/* const char* ssid     = "4G Wi-Fi 3Danmark-1CBA";
const char* password = "aircraft"; */
const char* ssid     = "network 42";
const char* password = "12345678";
 
AsyncWebServer server(80);
 
void setup(){
  Serial.begin(115200);
 
  if (!SPIFFS.begin(true)) {
      Serial.println("An error occurred while mounting SPIFFS");
  } else {
      Serial.println("SPIFFS mounted successfully");
  }

  if (SPIFFS.exists("/index.html")) {
    Serial.println("File exists.");
  } else {
      Serial.println("File does not exist.");
  }

  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
 
  Serial.println(WiFi.localIP());
 
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(SPIFFS, "/index.html", "text/html");
  });
 
  server.on("/script.js", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(SPIFFS, "/script.js", "text/javascript");
  });
 
  Serial.println("Starting server...");
  server.begin();
}
 
void loop(){}