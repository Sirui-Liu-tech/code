#include "SevSeg.h"

SevSeg sevseg;

byte numDigits = 4; 
byte digitPins[] = {2, 3, 12, 13}; 
byte segmentPins[] = {7, 6, 5, 10, 11, 8, 9, 4};
byte hardwareConfig = COMMON_CATHODE ; // 共阴极数码管

int numToShow = 0;
int count = 0;
int readValue = 0;
int showValueint = 0; 
double showvalue = 0;

void setup() {
  sevseg.begin(hardwareConfig, numDigits, digitPins, segmentPins);
}

void loop() {
  count = 0
  for(i=0;i<500;i++){
  readValue = analogRead(A0); 
  if(readValue>511){
    count++;
  }
  }
  showValueint = map(count, 0, 500, 0, 10000); 
  showvalue = showValueint/100.0
  sevseg.setNumber(showValue, 2); 
  sevseg.refreshDisplay(); 
}
