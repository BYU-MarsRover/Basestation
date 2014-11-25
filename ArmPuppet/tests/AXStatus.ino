
#define start 0xFF
#define rd 0x04
#define com 2

#define sendData(args)  (Serial1.write(args))    // Write Over Serial

void readGoalPos(unsigned char ID)
{
  unsigned char address = 30;
  unsigned char readLength = 2;
  
  unsigned char cs = ~(ID + 0x04 + wrt + readLength + address) & 0xFF;
  
  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(rd);
  sendData(address);
  sendData(readLength);
  sendData(cs);
  
}

void readCurrentPos(unsigned char ID)
{
  unsigned char address = 36;
  unsigned char readLength = 2;
  
  unsigned char cs = ~(ID + 0x04 + wrt + readLength + address) & 0xFF;
  
  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(rd);
  sendData(address);
  sendData(readLength);
  sendData(cs);
  
}

void readCurrentLoad(unsigned char ID)
{
  unsigned char address = 40;
  unsigned char readLength = 2;
  
  unsigned char cs = ~(ID + 0x04 + wrt + readLength + address) & 0xFF;
  
  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(rd);
  sendData(address);
  sendData(readLength);
  sendData(cs);
  
  
  digitalWrite(2, LOW);
  while(!Serial1.available())
  {}
  
  while(Serial1.available())
  {
    
    
  }
  
}

