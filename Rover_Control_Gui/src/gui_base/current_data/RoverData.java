package gui_base.current_data;

import gui_base.RoverBaseWindow;
import packet_models.RoverArmStatus;
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
	
	// Constructor
	public RoverData(RoverBaseWindow basewindow) {
		Root = basewindow;
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
	
}
