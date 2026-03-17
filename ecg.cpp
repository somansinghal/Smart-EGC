#include <WiFi.h>
#include <WebSocketsClient.h>

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";

WebSocketsClient webSocket;

int ecgPin = 34;

void setup(){

Serial.begin(115200);

WiFi.begin(ssid,password);

while(WiFi.status()!=WL_CONNECTED){
delay(500);
}

webSocket.begin("192.168.1.5",8000,"/ws");

}

void loop(){

int ecg = analogRead(ecgPin);

webSocket.sendTXT(String(ecg));

delay(8);

}