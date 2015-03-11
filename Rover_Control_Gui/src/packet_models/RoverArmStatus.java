package packet_models;

public class RoverArmStatus {

	private int dynamixelErrors;
	private int pid1Error;
	private int pid2Error;
	private int pid3Error;
	
	// Constructors
	public RoverArmStatus() {
		// for testing until full constructor determined
		dynamixelErrors = 10;
		pid1Error = 20;
		pid2Error = 30;
		pid3Error = 40;
	}
	
	public RoverArmStatus(RoverArmStatus oldcpy) {
		dynamixelErrors = oldcpy.getDynamixelErrors();
		pid1Error = oldcpy.getPid1Error();
		pid2Error = oldcpy.getPid2Error();
		pid3Error = oldcpy.getPid3Error();;
	}
	
	public RoverArmStatus(int dynamixelerrors, int pid1_error, int pid2_error, int pid3_error) {
		dynamixelErrors = dynamixelerrors;
		pid1Error = pid1_error;
		pid2Error = pid2_error;
		pid3Error = pid3_error;
	}

	// Other
	public String dataToString() {
		StringBuilder result = new StringBuilder();
		result.append("Dynamixel Errors: ");
		result.append(dynamixelErrors);
		result.append("\nPid1 Error: ");
		result.append(pid1Error);
		result.append("\nPid2 Error: ");
		result.append(pid2Error);
		result.append("\nPid3 Error: ");
		result.append(pid3Error);
		result.append("\n");
		return result.toString();
	}
	
	// Getters & Setters
	public int getDynamixelErrors() {
		return dynamixelErrors;
	}


	public void setDynamixelErrors(int dynamixelErrors) {
		this.dynamixelErrors = dynamixelErrors;
	}


	public int getPid1Error() {
		return pid1Error;
	}


	public void setPid1Error(int pid1Error) {
		this.pid1Error = pid1Error;
	}


	public int getPid2Error() {
		return pid2Error;
	}


	public void setPid2Error(int pid2Error) {
		this.pid2Error = pid2Error;
	}


	public int getPid3Error() {
		return pid3Error;
	}


	public void setPid3Error(int pid3Error) {
		this.pid3Error = pid3Error;
	}
	
}

/*
 * <field type="uint8_t"		name="systemState"	minValue="0" maxValue="3"	>System status code</field>
			<field type="uint16_t"	name="dynamixelErrors"							>Number of bad reads or writes to Dynamixel servos.</field>
			<field type="int16_t"		name="pid1_error"	minValue="-2000"	maxValue="2000">Error as in the error term, a scalar value.</field>
			<field type="int16_t"		name="pid2_error"	minValue="-2000"	maxValue="2000">Same as above, for the 2nd PID controller</field>
			<field type="int16_t"		name="pid3_error"	minValue="-2000"	maxValue="2000">Same as above, for the 3rd PID controller</field>
 */
