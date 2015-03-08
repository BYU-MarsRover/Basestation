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
	
	public RoverTabWindow(RoverBaseWindow basewindow) {
		Root = basewindow;
		HealthData = new RoverTextArea(Root);
		StatusData = new RoverTextArea(Root);
		ArmStatus = new RoverTextArea(Root);
		
		// set data
		HealthData.append(Root.getData().getHealth().dataToString());
		StatusData.append(Root.getData().getStatus().dataToString());
		ArmStatus.append(Root.getData().getArmStatus().dataToString());
		
		this.addTab("RoverHealth", HealthData);
		this.addTab("RoverStatus", StatusData);
		this.addTab("ArmStatus", ArmStatus);
	}

	public RoverBaseWindow getRoot() {
		return Root;
	}

	public void setRoot(RoverBaseWindow root) {
		Root = root;
	}
	
}
