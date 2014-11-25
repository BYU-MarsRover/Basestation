#include <DynamixelSerial1.h>

void setup(){
  Serial.begin(9600);
Dynamixel.begin(1000000,2);  // Inicialize the servo at 1Mbps and Pin Control 2
delay(1000);
}

int pos1;
int pos2;
int pos3;
int pos4;
void loop()
{
  
  delay(2);
  pos1 = Dynamixel.readPosition(1);
  pos2 = Dynamixel.readPosition(2);
  pos3 = Dynamixel.readPosition(3);
  pos4 = Dynamixel.readPosition(4);
  
  Serial.print(pos1);
  Serial.print(" ");
  Serial.print(pos2);
  Serial.print(" ");
  Serial.print(pos3);
  Serial.print(" ");
  Serial.print(pos4);
  Serial.print("\n");
  Serial.print("hi");
  
  //Dynamixel.move(1,random(200,800));
 //delay(2000);
 Dynamixel.moveSpeed(1,200,200);
  delay(2000);
  
}
