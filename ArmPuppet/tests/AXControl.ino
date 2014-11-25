
#define start 0xFF
#define testPin2 A1
//#define ID 0x01
#define wrt 0x03


#define sendData(args)  (Serial1.write(args))    // Write Over Serial


void AXLED(unsigned char ID, boolean Status)
{
  unsigned char cs = ~(ID + 0x04 + wrt + Status + 25);

  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(wrt);
  sendData(25);    //LED address
  sendData(Status);
  sendData(cs);

  return;
}

//setTorque

void Torque(unsigned char ID, boolean Status)
{
  unsigned char address = 24;

  unsigned char cs = ~(ID + 0x04 + wrt + Status + address);

  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(wrt);
  sendData(address);
  sendData(Status);
  sendData(cs);

  return;
}


//DynamixelClass::setCMargin(unsigned char ID, unsigned char CWCMargin, unsigned char CCWCMargin)

//Valid margins between 0 and 254
void CWCompMargin(unsigned char ID, int margin)
{
  unsigned char address = 26;

  unsigned char cs = ~(ID + 0x04 + wrt + margin + address);

  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(wrt);
  sendData(address);
  sendData(margin);
  sendData(cs);

  return;
}

//DynamixelClass::setCMargin(unsigned char ID, unsigned char CWCMargin, unsigned char CCWCMargin)

//Valid margins between 0 and 254
void CCWCompMargin(unsigned char ID, int margin)
{
  unsigned char address = 27;

  unsigned char cs = ~(ID + 0x04 + wrt + margin + address);

  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(wrt);
  sendData(address);
  sendData(margin);
  sendData(cs);

  return;
}

//int DynamixelClass::setCSlope(unsigned char ID, unsigned char CWCSlope, unsigned char CCWCSlope)

//Valid slopes between 0 and 254
void CWCompSlope(unsigned char ID, int slope)
{
  unsigned char address = 28;

  unsigned char cs = ~(ID + 0x04 + wrt + slope + address);

  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(wrt);
  sendData(address);
  sendData(slope);
  sendData(cs);

  return;
}

//int DynamixelClass::setCSlope(unsigned char ID, unsigned char CWCSlope, unsigned char CCWCSlope)

//Valid slopes between 0 and 254
void CCWCompSlope(unsigned char ID, int slope)
{
  unsigned char address = 29;

  unsigned char cs = ~(ID + 0x04 + wrt + slope + address);

  sendData(start);
  sendData(start);
  sendData(ID);
  sendData(0x04);  //Length
  sendData(wrt);
  sendData(address);
  sendData(slope);
  sendData(cs);

  return;
}

//Tells the servo to go to the specified location.
//move()

void goTo(unsigned char ID, int location)
{
  unsigned char address = 30;

  unsigned char lower = location & 0xFF;

  unsigned char upper = (location >> 8) & 0xFF;

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

void torqueLimit(unsigned char ID, int limit)
{
  unsigned char address = 34;

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

void setSpeed(unsigned char ID, int limit)
{
  unsigned char address = 32;

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

//value between 0 and 1023
void setPunch(unsigned char ID, int punch)
{
  unsigned char address = 32;

  unsigned char lower = punch & 0xFF;

  unsigned char upper = (punch >> 8) & 0xFF;

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


