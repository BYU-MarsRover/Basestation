package gui_base.current_data;

import gui_base.RoverBaseWindow;
import packet_models.RoverArmStatus;
import packet_models.RoverGPS;
import packet_models.RoverIMU;
import packet_models.RoverStatus;
import packet_models.RoverSysHealth;

/**
 * 
 * @author Nathan Warner
 *	Contains all the current data from the rover. This will need functions to update the pieces of
 * It's pieces. This is also a collection of all the data being displayed on the GUI. If the data isn't
 * here, then it isn't being displayed on the GUI.
 * 
 */
public class RoverData {

	private RoverBaseWindow Root;
	private RoverArmStatus ArmStatus;
	private RoverStatus Status;
	private RoverSysHealth Health;
	private RoverIMU IMU;
	private RoverGPS GPS;
	
	// Constructors
	public RoverData(RoverBaseWindow basewindow) {
		Root = basewindow;
	}

	// Functions
	/**
	 * Updates all the displays on the GUI with the current set of data values
	 * Call this any time data values are changed.
	 */
	public void updateDisplayedData() {
		Root.getBaseDisplay().getComponentB().getComponentA().getComponentB().selectAll();
		Root.getBaseDisplay().getComponentB().getComponentA().getComponentB().replaceSelection(Root.getData().getGPS().dataToString());
		// uncomment the next two lines when you know which class they are actually pulling data from.			|
//		Root.getBaseDisplay().getComponentB().getComponentA().getComponentA().selectAll();					//  V
//		Root.getBaseDisplay().getComponentB().getComponentA().getComponentA().replaceSelection(Root.getData().getStatus().dataToString());
		Root.getBaseDisplay().getComponentB().getComponentA().repaint();
		Root.getBaseDisplay().getComponentB().getComponentB().updateDisplayedData();		// updates data displayed in tabbed pane
	}
	
	// Getters & Setters
	public RoverBaseWindow getRoot() {
		return Root;
	}

	public void setRoot(RoverBaseWindow root) {
		Root = root;
	}

	public RoverArmStatus getArmStatus() {
		return ArmStatus;
	}

	public void setArmStatus(RoverArmStatus armStatus) {
		ArmStatus = armStatus;
	}

	public RoverStatus getStatus() {
		return Status;
	}

	public void setStatus(RoverStatus status) {
		Status = status;
	}

	public RoverSysHealth getHealth() {
		return Health;
	}

	public void setHealth(RoverSysHealth health) {
		Health = health;
	}

	public RoverIMU getIMU() {
		return IMU;
	}

	public void setIMU(RoverIMU iMU) {
		IMU = iMU;
	}

	public RoverGPS getGPS() {
		return GPS;
	}

	public void setGPS(RoverGPS gPS) {
		GPS = gPS;
	}
	
}
