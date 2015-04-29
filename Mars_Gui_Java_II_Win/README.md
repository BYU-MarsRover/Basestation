## Overview

I wrote a batch script that should launch the xbox controller script, the server and the client.  If you give the batch script parameters, you can run it pointing at a specific IP.  if no parameters are provided the client and server for both the arm and base station will run on localhost 27015.

If you were wanting to send packets to the actual rover you would run this from the command line:

**run.bat 192.168.10.4 192.168.10.3 27015**

I will be dropping off the xbox controller at the lab today, so if anyone wants to get the code and controller and test out my code that's where they can find the controller. We will probably need to invert some of the values being sent either on the base station, or the PSoC to get the full functionality that we want.

## Control Schema

**BACK button:** 

Enables arm_control mode, disables main_board control mode and wrist_control mode. (This button toggles)

**START button:**

Enable wrist_control mode, disables main_board control mode and arm_control mode. (This button toggles)

**LEFT TRIGGER:**

Enables arm_control mode, disables main_board control mode and wrist_control mode. (This is a on-off functionality)

**RIGHT TRIGGER:** 

Enables wrist_control mode, disables main_board control mode and arm_control mode. (This is an on-off functionality)

**MOVEMENT:**

Tank style controls using the left and right joystick are employed when the controller is in main_board control mode (Neither left or right triggers are held, and the neither back or start have been toggled on.)

The left joystick will send packet data controlling the left wheels. (Forward and reverse)

The right joystick will send packet data controlling the right wheels. (Forward and reverse)

**CAMERA MOVEMENT:**

The camera controls are enabled when the controller is in the main_board control mode described above.

The D-pad hat - x axis controls camera pan. (left and right)

The D-pad had - y axis controls camera tilt. (up and down)

**ARM MOVEMENT:**

The arm controls are enabled when the controller is in arm_control mode. (back button is toggled on, or the left trigger is pressed)

The left joystick - x axis controls the arm_turret. (left and right)

The left joystick - y axis controls the shoulder. (up and down)

The right joystick - y axis controls the elbow. (up and down)

**WRIST MOVEMENT:**

The wrist controls are enabled when the controller is in wrist_control mode. (start button is toggled on, or right trigger is pressed)

The right joystick - x axis controls wrist rotation. (counter-clockwise and clockwise)

The right joystick - y axis controls wrist tilt. (up and down)

All the currently used packet formatting is easily read by looking at the packet mask constants in src/python/xbox.py.
