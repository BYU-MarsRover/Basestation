package gui_base.formats;

import gui_base.RoverBaseWindow;
import gui_base.displays.RoverTextArea;

import javax.swing.JTabbedPane;

@SuppressWarnings("serial")
public class RoverTabWindow extends JTabbedPane {

	private RoverBaseWindow Root;
	private RoverTextArea HealthData;
	private RoverTextArea StatusData;
	private RoverTextArea ArmStatus;
	private RoverTextArea IMU;

	// Constructors
	public RoverTabWindow(RoverBaseWindow basewindow) {
		Root = basewindow;
		HealthData = new RoverTextArea(Root);
		StatusData = new RoverTextArea(Root);
		ArmStatus = new RoverTextArea(Root);
		IMU = new RoverTextArea(Root);

		// set data
		HealthData.append(Root.getData().getHealth().dataToString());
		StatusData.append(Root.getData().getStatus().dataToString());
		ArmStatus.append(Root.getData().getArmStatus().dataToString());
		IMU.append(Root.getData().getIMU().dataToString());

		this.addTab("RoverHealth", HealthData);
		this.addTab("RoverStatus", StatusData);
		this.addTab("ArmStatus", ArmStatus);
		this.addTab("IMU", IMU);
	}

	// Functions
	public void updateDisplayedData() {
		HealthData.selectAll();
		HealthData.replaceSelection(Root.getData().getHealth().dataToString());
		StatusData.selectAll();
		StatusData.replaceSelection(Root.getData().getStatus().dataToString());
		ArmStatus.selectAll();
		ArmStatus.replaceSelection(Root.getData().getArmStatus().dataToString());
		IMU.selectAll();
		IMU.replaceSelection(Root.getData().getIMU().dataToString());
		this.repaint();
	}
	
	// Getters & Setters
	public RoverBaseWindow getRoot() {
		return Root;
	}

	public void setRoot(RoverBaseWindow root) {
		Root = root;
	}

	public RoverTextArea getHealthData() {
		return HealthData;
	}

	public void setHealthData(RoverTextArea healthData) {
		HealthData = healthData;
	}

	public RoverTextArea getStatusData() {
		return StatusData;
	}

	public void setStatusData(RoverTextArea statusData) {
		StatusData = statusData;
	}

	public RoverTextArea getArmStatus() {
		return ArmStatus;
	}

	public void setArmStatus(RoverTextArea armStatus) {
		ArmStatus = armStatus;
	}

	public RoverTextArea getIMU() {
		return IMU;
	}

	public void setIMU(RoverTextArea iMU) {
		IMU = iMU;
	}

}
