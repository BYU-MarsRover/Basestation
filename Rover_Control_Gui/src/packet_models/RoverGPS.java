package packet_models;

public class RoverGPS {

	private int XCoordinate;
	private int YCoordinate;
	
	// Constructors
	public RoverGPS() {
		XCoordinate = 3248;
		YCoordinate = 6339;
	}
	
	// Other
	public String dataToString() {
		StringBuilder result = new StringBuilder();
		result.append("Rover Position:\nX Coordinate: ");
		result.append(XCoordinate);
		result.append("\nY Coordinate: ");
		result.append(YCoordinate);
		result.append("\n");
		return result.toString();
	}

	// Getters & Setters
	public int getXCoordinate() {
		return XCoordinate;
	}

	public void setXCoordinate(int xCoordinate) {
		XCoordinate = xCoordinate;
	}

	public int getYCoordinate() {
		return YCoordinate;
	}

	public void setYCoordinate(int yCoordinate) {
		YCoordinate = yCoordinate;
	}
	
}
