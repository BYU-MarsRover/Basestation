

#define start 0xFF
#define wrt 0x03

#define sendData(args)  (Serial1.write(args))    // Write Over Serial


//Baud rate = 2000000/(baud + 1)
void setDefBaud(unsigned char ID, int baud)
{
  unsigned char address = 4;
  unsigned char cs = ~(ID + 0x04 + wrt + baud + address);
  
  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(wrt);
  sendData(address); 
  sendData(baud);
  sendData(cs);
  
  return;
}

void setDefID(unsigned char ID, unsigned char newID)
{
  unsigned char address = 3;
  unsigned char length = 4;
  unsigned char cs = ~(ID + length + wrt + newID + address);
  
  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(length);  //Length
  sendData(wrt);
  sendData(address); 
  sendData(newID);
  sendData(cs);
  
  return;
}

//delay time = 2uSec * delayT
void setReturnDelay(unsigned char ID, int delayT)
{
  unsigned char address = 5;
  unsigned char cs = ~(ID + 0x04 + wrt + delayT + address);
  
  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(wrt);
  sendData(address); 
  sendData(delayT);
  sendData(cs);
  
  return;
}

void setCWLimit(unsigned char ID, int limit)
{
  unsigned char address = 6;
  
  unsigned char lower = limit & 0xFF;
  
  unsigned char upper = (limit >> 8) & 0xFF;
  
  unsigned char cs = ~(ID + 0x05 + wrt + lower + upper + address) & 0xFF;
  
  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x05);  //Length
  sendData(wrt);
  sendData(address);
  sendData(lower);
  sendData(upper);
  sendData(cs);
  
}


void setCCWLimit(unsigned char ID, int limit)
{
  unsigned char address = 8;
  
  unsigned char lower = limit & 0xFF;
  
  unsigned char upper = (limit >> 8) & 0xFF;
  
  unsigned char cs = ~(ID + 0x05 + wrt + lower + upper + address) & 0xFF;
  
  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x05);  //Length
  sendData(wrt);
  sendData(address);
  sendData(lower);
  sendData(upper);
  sendData(cs);
  
}

//Degrees C.
void setTempLimit(unsigned char ID, int tempLimit)
{
  unsigned char address = 11;
  unsigned char cs = ~(ID + 0x04 + wrt + tempLimit + address);
  
  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(wrt);
  sendData(address); 
  sendData(tempLimit);
  sendData(cs);
  
  return;
}

void setMinVoltage(unsigned char ID, int minVoltage)
{
  unsigned char address = 12;
  unsigned char cs = ~(ID + 0x04 + wrt + minVoltage + address);
  
  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(wrt);
  sendData(address); 
  sendData(minVoltage);
  sendData(cs);
  
  return;
}

void setMaxVoltage(unsigned char ID, int maxVoltage)
{
  unsigned char address = 13;
  unsigned char cs = ~(ID + 0x04 + wrt + maxVoltage + address);
  
  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(wrt);
  sendData(address); 
  sendData(maxVoltage);
  sendData(cs);
  
  return;
}

void setMaxTorque(unsigned char ID, int limit)
{
  unsigned char address = 14;
  
  unsigned char lower = limit & 0xFF;
  
  unsigned char upper = (limit >> 8) & 0xFF;
  
  unsigned char cs = ~(ID + 0x05 + wrt + lower + upper + address) & 0xFF;
  
  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x05);  //Length
  sendData(wrt);
  sendData(address);
  sendData(lower);
  sendData(upper);
  sendData(cs);
  
}

void setStatusReturn(unsigned char ID, int returnT)
{
  unsigned char address = 13;
  unsigned char cs = ~(ID + 0x04 + wrt + returnT + address);
  
  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(wrt);
  sendData(address); 
  sendData(returnT);
  sendData(cs);
  
  return;
}

//Set bit should be 1, 2, 3, etc.
//Bit 0: Voltage error, 1: angle limit, 2: overheat, 3: range, 4: checksum, 5: overload
//6: instruction
//This only allows one error to be set at a time.
void setLEDAlarm(unsigned char ID, int SetBit)
{
  unsigned char address = 17;
  
  unsigned char cs = ~(ID + 0x04 + wrt + (0x01 << SetBit) + address);
  
  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(wrt);
  sendData(address); 
  sendData(0x01 << SetBit);
  sendData(cs);
  
  return;
}

//Set bit should be a hex number corresponding to the bits to be set. EG 0x01 for voltage.
//Bit 0: Voltage error, 1: angle limit, 2: overheat, 3: range, 4: checksum, 5: overload
//6: instruction
//This only allows one error to be set at a time.
void setLEDAlarm(unsigned char ID, unsigned char SetBit)
{
  unsigned char address = 18;
  
  unsigned char cs = ~(ID + 0x04 + wrt + SetBit + address);
  
  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(wrt);
  sendData(address); 
  sendData(SetBit);
  sendData(cs);
  
  return;
}



