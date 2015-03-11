package packet_models;

public class RoverSysHealth {
	
	private int systemTimeStamp;
	private String systemState;
	private int cpuLoad;				// minValue = 0, maxValue = 1000
	private int busErrors;
	private int ethernetErrors;
	private int someOtherMetric;
	
	// Constructors
	public RoverSysHealth() {
			systemTimeStamp = 10;
			systemState = "In testing";
			cpuLoad = 12;
			busErrors = 14;
			ethernetErrors = 16;
			someOtherMetric = 18;
	}
	
	public RoverSysHealth(RoverSysHealth oldcpy) {
		systemTimeStamp = oldcpy.getSystemTimeStamp();
		systemState = oldcpy.getSystemState();
		cpuLoad = oldcpy.getCpuLoad();
		busErrors = oldcpy.getBusErrors();
		ethernetErrors = oldcpy.getEthernetErrors();
		someOtherMetric = oldcpy.getSomeOtherMetric();
	}
	
	public RoverSysHealth(int systimestamp, String sysstate, int cpuload, int buserrors, int etherneterrors, int someothermetric) {
		systemTimeStamp = systimestamp;
		systemState = sysstate;
		cpuLoad = cpuload;
		busErrors = buserrors;
		ethernetErrors = etherneterrors;
		someOtherMetric = someothermetric;
	}

	// Other
	public String dataToString() {
		StringBuilder result = new StringBuilder();
		result.append("TimeStamp: ");
		result.append(systemTimeStamp);
		result.append("\nSystem State: ");
		result.append(systemState);
		result.append("\nCPU Load: ");
		result.append(cpuLoad);
		result.append("\nBus Errors: ");
		result.append(busErrors);
		result.append("\nEthernet Errors: ");
		result.append(ethernetErrors);
		result.append("\nSome Other Metric: ");
		result.append(someOtherMetric);
		result.append("\n");
		return result.toString();
	}
	
	// Getters & Setters
	public int getSystemTimeStamp() {
		return systemTimeStamp;
	}

	public void setSystemTimeStamp(int systemTimeStamp) {
		this.systemTimeStamp = systemTimeStamp;
	}

	public String getSystemState() {
		return systemState;
	}

	public void setSystemState(String systemState) {
		this.systemState = systemState;
	}

	public int getCpuLoad() {
		return cpuLoad;
	}

	public void setCpuLoad(int cpuLoad) {
		this.cpuLoad = cpuLoad;
	}

	public int getBusErrors() {
		return busErrors;
	}

	public void setBusErrors(int busErrors) {
		this.busErrors = busErrors;
	}

	public int getEthernetErrors() {
		return ethernetErrors;
	}

	public void setEthernetErrors(int ethernetErrors) {
		this.ethernetErrors = ethernetErrors;
	}

	public int getSomeOtherMetric() {
		return someOtherMetric;
	}

	public void setSomeOtherMetric(int someOtherMetric) {
		this.someOtherMetric = someOtherMetric;
	}
	
}
