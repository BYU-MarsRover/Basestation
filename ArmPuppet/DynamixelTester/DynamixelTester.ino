#include <DynamixelSerial1.h> 

const int debugPin = 13;
// const uint8_t baudList [] = {1,3,4,7,9,16,34,103,207};
const uint32_t baudList [] = {1000000,500000,400000,250000,200000,115200,57600,19200,9600};
const uint8_t BAUDCOUNT = (sizeof(baudList)/4);


static uint32_t timestamp;
static uint32_t baud;

static volatile struct{
	uint16_t turret;
	uint16_t shoulder;
	uint16_t elbow;
	uint16_t wristRotate;
	uint16_t wristPitch;
	uint16_t effector;
	uint16_t lock;
} pArm;

void setup(){
	Serial.begin(115200);
	pinMode(debugPin,OUTPUT);
	
	// Duplex Serial Test
	pinMode(16, OUTPUT);
	pinMode(17, INPUT);
	digitalWrite(16, HIGH);
	Serial.println(digitalRead(17));
	digitalWrite(16, LOW);
	Serial.println(digitalRead(17));
	pinMode(16, INPUT);
	Serial.println(digitalRead(17));
	digitalWrite(16, HIGH);
	
	// pinMode(uartTxPin,INPUT);
	
	Serial.print("BaudList: ");
	Serial.println(BAUDCOUNT);
	Dynamixel.begin(1000000,debugPin);
	// Serial2.begin(115200);
	// Serial2.println("Works");
	delay(1000);
}

void loop(){
	
	// pArm.turret			+= 5;
	// pArm.shoulder		+= 17;
	// pArm.elbow			+= 47;
	// pArm.wristRotate	+= 17;
	// pArm.wristPitch		+= 101;
	// pArm.effector		+= 3;
	
	
	
	pArm.turret			= Dynamixel.readPosition(0);	// [ 75:950]	Turned Left	-> Turned Right
	pArm.shoulder		= Dynamixel.readPosition(1);	// [830:460]	Laying Down	-> Erect
	pArm.elbow			= Dynamixel.readPosition(2);	// [860:160]	Tucked In	-> Bent Out
	pArm.wristRotate	= Dynamixel.readPosition(3);	// [200:820]	Left 90	deg	-> Right 90 deg
	pArm.wristPitch		= Dynamixel.readPosition(4);	// [200:820]	Pitch Down	-> Pitch Up
	pArm.effector		= analogRead(A8);  // (analogRead(A8)  > 500)? 1 : 0; // Dynamixel.readPosition(5);
	pArm.lock			= analogRead(A13); // (analogRead(A13) > 500)? 1 : 0;
	
	
	
	armReport();
	
	
	static uint8_t ledToggle;
	ledToggle = (ledToggle)? 0 : 1;
	for(uint8_t i=0; i<5; i++){
		Dynamixel.ledStatus(   i, ledToggle); //(pArm.lock <500)? 0 : 1
		Dynamixel.torqueStatus(i, (pArm.lock <500)? 0 : 1);
		
	}
	
	
	/*
	
	
	// delay(20);
	static uint8_t addr = 0;
	
	// Serial.println("LoopStart");
	// for(uint8_t i=0; i<BAUDCOUNT; i++){
	// for(uint8_t i=0; i<250; i += (i<30)? 1 : ((i<100)? 2 : 5) ){
	for(uint8_t i=0; i<255; i++){
		// armReport();
		baud = 2000000 / (i+1);
		// uint32_t baud = 2000000 / (i+1);
		// uint32_t baud = 1000000;
		
		// Serial.println(baudList[i]);
		//Dynamixel.begin(baudList[i],debugPin);
		// Serial.println(i);
		Serial.println(baud);
		Dynamixel.begin(baud,debugPin);
		delay(110);
		
		// addr = (addr >= 0xFE)? 0 : addr +1;
		// for(uint8_t addr=0; addr<=0xFE; addr++){
		// for(uint8_t addr=0xFB; addr<=0xFE; addr++){
			// Dynamixel.setID(addr, 0xFB);
			// Dynamixel.setSRL(addr, 0x02);
			// Dynamixel.setRDT(addr, 0xFA);
			// Dynamixel.reset(0xFE);
			// delay(10);
			int8_t response = Dynamixel.ping(1);
			Dynamixel.ledStatus(addr,0x01);
			// Serial.print("Response ");
			
			if( (response != -1) ){ // || (addr == 0x00) ){
				Serial.print("\t");
				Serial.print(addr);
				Serial.print(" = ");
				Serial.print(response);
				Serial.print("\r\n");
				// Dynamixel.setID(addr, 0x0A);
				// Dynamixel.setBD(addr, 0x01);
			}
			
			// Dynamixel.setBD(addr, 0x01);
		Dynamixel.end();
			delay(2);
		// }
		
		// delay(100);
	}	
	Dynamixel.begin(1000000,debugPin);
	delay(2);
	
	*/
}



void armReport(void){

	if(millis() >= (timestamp+100)){
		timestamp = millis();
		
		uint16_t turret			= pArm.turret;
		uint16_t shoulder		= pArm.shoulder;
		uint16_t elbow			= pArm.elbow;
		uint16_t wristRotate	= pArm.wristRotate;
		uint16_t wristPitch		= pArm.wristPitch;
		uint16_t effector		= pArm.effector;
		uint16_t lock			= pArm.lock;
		
		uint16_t checkSum = turret^shoulder^elbow^wristRotate^wristPitch^effector^lock;
		
		Serial.print("$PUPRPT,");
		Serial.print(turret);
		// Serial.print(baud);
		Serial.print(",");
		Serial.print(shoulder);
		Serial.print(",");
		Serial.print(elbow);
		Serial.print(",");
		Serial.print(wristRotate);
		Serial.print(",");
		Serial.print(wristPitch);
		Serial.print(",");
		Serial.print(effector);
		Serial.print(",");
		Serial.print(lock);
		Serial.print(",");
		Serial.print(checkSum);
		Serial.print("*");
		Serial.print("\r\n");
	
	
	
	}
}
