import serial






ser = serial.Serial('COM5', 1000000, timeout=1)
# ser.port     = port
# ser.baudrate = baudrate
# ser.parity   = options.parity
# ser.rtscts   = options.rtscts
# ser.xonxoff  = options.xonxoff
# ser.timeout  = 1     # required so that the reader thread can exit

print ser.name

data = {0xFF,0xFF, 0xFE, 0x02, 
checksum = 

ser.write()

ser.close();


# try:
	# ser.open()
# except serial.SerialException, e:
	# sys.stderr.write("Could not open serial port %s: %s\n" % (ser.portstr, e))
	# sys.exit(1)


# self.serial.write(data) 




# data = self.serial.read(1)              # read one, blocking
	# n = self.serial.inWaiting()             # look if there is more
	# if n:
		# data = data + self.serial.read(n)   # and get as much as possible
	# if data:












