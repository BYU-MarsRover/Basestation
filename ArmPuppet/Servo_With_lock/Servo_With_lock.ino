#include <DynamixelSerial1.h> 

const int switchPin = 43;

void setup(){
	pinMode(switchPin,INPUT);
	Serial.begin(9600);
	Dynamixel.begin(1000000,2);  // Inicialize the servo at 1Mbps and Pin Control 2
	delay(1000);
}

int pos1=500;
int pos2=500;
int pos3=500;
int pos4=500;

int state=0;

void loop(){
	delay(2);
	pos1 = Dynamixel.readPosition(1);
	pos2 = Dynamixel.readPosition(2);
	pos3 = Dynamixel.readPosition(3);
	pos4 = Dynamixel.readPosition(4);
	state= digitalRead(switchPin);
	
	while (state== HIGH){
		Serial.println ("000000");
		Dynamixel.move(1,pos1);
		Dynamixel.move(2,pos2);
		Dynamixel.move(3,pos3);
		Dynamixel.move(4,pos4);
		state= digitalRead(switchPin);
	}
	Dynamixel.move(1,pos1+10);
	Dynamixel.move(2,pos2+10);
	Dynamixel.move(3,pos3+10);
	Dynamixel.move(4,pos4+10);
  

	Serial.write(pos1);
	Serial.print(" ");
	Serial.write(pos2);
	Serial.print(" ");
	Serial.write(pos3);
	Serial.print(" ");
	Serial.write(pos4);
	Serial.println(" ");
   
  
}
