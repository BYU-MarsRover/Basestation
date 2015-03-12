package packet_models;

public class RoverIMU {
	private int Yacc;
	private int Zacc;
	private int Xgyro;
	private int Ygyro;
	private int Zgyro;
	private int Xmag;
	private int Ymag;
	private int Zmag;
	
	// Constructors
	public RoverIMU () {
		Yacc = 10;
		Zacc = 20;
		Xgyro = 30;
		Ygyro = 40;
		Zgyro = 50;
		Xmag = 60;
		Ymag = 70;
		Zmag = 80;
	}

	// General Functions
	public String dataToString() {
		StringBuilder result = new StringBuilder();
		result.append("Y acceleration: ");
		result.append(Yacc);
		result.append("\nZ acceleration: ");
		result.append(Zacc);
		result.append("\nX gyro: ");
		result.append(Xgyro);
		result.append("\nY gyro: ");
		result.append(Ygyro);
		result.append("\nZ gyro: ");
		result.append(Zgyro);
		result.append("\nX mag: ");
		result.append(Xmag);
		result.append("\nY mag: ");
		result.append(Ymag);
		result.append("\nZ mag: ");
		result.append(Zmag);
		result.append("\n");
		return result.toString();
	}
	
	// Getters & Setters
	public int getYacc() {
		return Yacc;
	}

	public void setYacc(int yacc) {
		Yacc = yacc;
	}

	public int getZacc() {
		return Zacc;
	}

	public void setZacc(int zacc) {
		Zacc = zacc;
	}

	public int getXgyro() {
		return Xgyro;
	}

	public void setXgyro(int xgyro) {
		Xgyro = xgyro;
	}

	public int getYgyro() {
		return Ygyro;
	}

	public void setYgyro(int ygyro) {
		Ygyro = ygyro;
	}

	public int getZgyro() {
		return Zgyro;
	}

	public void setZgyro(int zgyro) {
		Zgyro = zgyro;
	}

	public int getXmag() {
		return Xmag;
	}

	public void setXmag(int xmag) {
		Xmag = xmag;
	}

	public int getYmag() {
		return Ymag;
	}

	public void setYmag(int ymag) {
		Ymag = ymag;
	}

	public int getZmag() {
		return Zmag;
	}

	public void setZmag(int zmag) {
		Zmag = zmag;
	}
	
}

/*
 * 	<field type="int16_t" name="xacc"	>X Acceleration, Front+</field>
			<field type="int16_t" name="yacc"	>Y Acceleration, Starboard+</field>
			<field type="int16_t" name="zacc"	>Z Acceleration, Down+</field>
			<field type="int16_t" name="xgyro"	>X Rotation Rate</field>
			<field type="int16_t" name="ygyro"	>Y Rotation Rate</field>
			<field type="int16_t" name="zgyro"	>Z Rotation Rate</field>
			<field type="int16_t" name="xmag"	>X B-Field Component</field>
			<field type="int16_t" name="ymag"	>Y B-Field Component</field>
			<field type="int16_t" name="zmag"	>Z B-Field Component</field>
 */