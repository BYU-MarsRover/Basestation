#define com 2

void setup()
{
  Serial1.begin(1000000);
  
  Serial.begin(9600);
  pinMode(com, OUTPUT);
  
  delay(1000);
  
  
}

void loop()
{
  
  //setDefID(1, 4);
  
  digitalWrite(com, HIGH);
  
  AXLED(1, false);
  
  
  delay(500);
  
  AXLED(1, true);
  
  delay(500);
  
  //goTo(4, 512);
  setSpeed(3, 100);
  setSpeed(2, 100);
  setSpeed(4, 100);
  setSpeed(1, 200);
  goTo(4, random(200, 800)); // 180-860
  delay(5);
  goTo(3, random(200, 800));  //180-840
  delay(5);
  goTo(2, random(500, 700));  //This is mounted 90º off (clockwise looking from the top.) 480-800
  delay(5);
  goTo(1, random(300, 800));  //0-1024
  /*
  setSpeed(1, 1023);
  
  CCWCompMargin(1, 50);
  CWCompMargin(1, 0);
  
  //CWCompSlope(1, 10);
  //CCWCompSlope(1, 250);
  
  //goTo(2, random(300, 800));
  
  torqueLimit(1, 1000);
  */
  
  
  
  
}
