## Summary of Basestation Code
This list will go down from most recently developed code 
to oldest/least developed code.

### Mars_Gui_Java_II_Win
**This is the windows implementation of the hybrid Python/Java base station.**
The basics of this code are:

**Xbox Controller Code is Implemented in Python**

Controller data is taken in using the pygame module, placed in the correct 
packet format and placed into a fifo style file at bin/xbox_to_java.

**A client is implemented in Java to send packets to the address given from the command line. **

This program reads from the aforementioned file (bin/xbox_to_java) and sends the packets to the adress given in the command line.

**A Server is implemented in Java to display packets sent to the base station.**

This server should receive packets sent from the rover to the base station. If packets are sent from the client to localhost, these packets will show up on the server.

**All three programs are launched simultaneously by using the run.bat script.**

### Mars_Gui_Java_II
**This is the most recent linux version of the hybrid Python/Java base station.**

This code is essentially the same as the Windows code, only it is run using a shell script instead of a batch script. It also uses a linux pipe instead of a file to communicate between python and java.

### Rover_Control_Gui
** This GUI will show the current status of the rover at all times based on the packets sent by the rover to the** ** base station.**

### Mars_Gui_Python
** This was an initial attempt to build the entire base station in python.**

### Mars_Gui_Java
** This was the first attempts to build the entire base station in Java.**
