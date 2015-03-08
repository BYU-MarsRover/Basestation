package packet_models;

public class RoverStatus {

	private int roverVoltage;
	private int roverCurrent;
	private int mAhCounter;
	private int ubntLinkInteg;
	private int dragonLinkRSSI;
	
	// Constructors
	public RoverStatus() {
		roverVoltage = 100;
		roverCurrent = 200;
		mAhCounter = 300;
		ubntLinkInteg = 400;
		dragonLinkRSSI = 500;
	}
	
	public RoverStatus(RoverStatus oldcpy) {
		roverVoltage = oldcpy.getRoverVoltage();
		roverCurrent = oldcpy.getRoverCurrent();
		mAhCounter = oldcpy.getmAhCounter();
		ubntLinkInteg = oldcpy.getUbntLinkInteg();
		dragonLinkRSSI = oldcpy.getDragonLinkRSSI();
	}
	
	public RoverStatus(int rovervoltage, int rovercurrent, int mahcounter, int ubntlinkinteg, int dragonlinkrssi) {
		roverVoltage = rovervoltage;
		roverCurrent = rovercurrent;
		mAhCounter = mahcounter;
		ubntLinkInteg = ubntlinkinteg;
		dragonLinkRSSI = dragonlinkrssi;
	}

	// Other
	public String dataToString() {
		StringBuilder result = new StringBuilder();
		result.append("Rover Voltage: ");
		result.append(roverVoltage);
		result.append("\nRover Current: ");
		result.append(roverCurrent);
		result.append("\nMAh Counter: ");
		result.append(mAhCounter);
		result.append("\nUbnt Link Integ: ");
		result.append(ubntLinkInteg);
		result.append("\nDragon Link RSSI: ");
		result.append(dragonLinkRSSI);
		return result.toString();
	}
	
	// Getters & Setters
	public int getRoverVoltage() {
		return roverVoltage;
	}

	public void setRoverVoltage(int roverVoltage) {
		this.roverVoltage = roverVoltage;
	}

	public int getRoverCurrent() {
		return roverCurrent;
	}

	public void setRoverCurrent(int roverCurrent) {
		this.roverCurrent = roverCurrent;
	}

	public int getmAhCounter() {
		return mAhCounter;
	}

	public void setmAhCounter(int mAhCounter) {
		this.mAhCounter = mAhCounter;
	}

	public int getUbntLinkInteg() {
		return ubntLinkInteg;
	}

	public void setUbntLinkInteg(int ubntLinkInteg) {
		this.ubntLinkInteg = ubntLinkInteg;
	}

	public int getDragonLinkRSSI() {
		return dragonLinkRSSI;
	}

	public void setDragonLinkRSSI(int dragonLinkRSSI) {
		this.dragonLinkRSSI = dragonLinkRSSI;
	}
	
}

/*
 * <field type="systemState_t"	name="systemState"		minValue="0"		maxValue="3"		>System status code, see enum definition</field>
			<field type="uint16_t"			name="roverVoltage"		minValue="0"		maxValue="60000"	>Voltage in mV, Ex: 12450 means 12.450 Volts</field>
			<field type="int16_t"				name="roverCurrent"		minValue="-20000"	maxValue="20000"	>Current in 10mA, Ex: 16500 means 165.00 Amps</field>
			<field type="int32_t"				name="mAhCounter"		minValue="0"		maxValue="100000"	>Battery used in mAh</field>
			<field type="uint16_t"			name="ubntLinkInteg"	minValue="0"		maxValue="1000"		>100% means perfect link, 0% is lost link, in 0.1% units</field>
			<field type="uint16_t"			name="dragonLinkRSSI"	minValue="0"		maxValue="1000"
 */