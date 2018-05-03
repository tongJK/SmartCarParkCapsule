
#include <Wire.h>
#define SLAVE_ADDRESS 0x04

char positions[2];
char f;
int state = 0;
int flr = 0;
int slt = 0;


void setup() {
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  //  Wire.onRequest(sendData);
}

void loop() {
  delay(100);
} 


void receiveData(int byteCount) {
  int i = 0;
  while (Wire.available()) {
    positions[i] = Wire.read(); 
    i++;
    
  }
  positions[i] = '\0';
  f = positions[0];
  Serial.print(positions);
  Serial.print(f/10);

}  

void sendData() {
  Wire.write(positions);
}

