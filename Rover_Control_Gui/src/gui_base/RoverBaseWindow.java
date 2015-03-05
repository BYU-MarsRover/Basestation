package gui_base;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Toolkit;

import gui_base.control_panel.RoverSettings;
import gui_base.current_data.RoverData;
import gui_base.displays.RoverVideoDisplay;
import gui_base.formats.RoverSplitWindow;
import gui_base.formats.RoverTabWindow;

import javax.swing.JFrame;

import packet_models.RoverArmStatus;
import packet_models.RoverStatus;
import packet_models.RoverSysHealth;

/**
 * 
 * @author Nathan Warner
 * This is the base window for the GUI. Everything is built up from here. All sub-Classes should have
 * Access to this class. Through it all other classes will have access to:
 * - The GUI Listener (for user input)
 * - All data to be displayed
 * - A link to all other parts of the GUI for controls
 *
 */
@SuppressWarnings("serial")
public class RoverBaseWindow extends JFrame {
	
	private RoverGUIListener MainListener;
	private RoverSettings Settings;
	private RoverSplitWindow BaseDisplay;
	private RoverData Data;
//	private ClientPortal Portal;
	private int WindowWidth;
	private int WindowHeight;
	
	public RoverBaseWindow() {

		// Set Window Format
		Toolkit kit = Toolkit.getDefaultToolkit();
		setTitle("Mars Rover Control");
		Dimension screenSize = kit.getScreenSize();
		WindowWidth = screenSize.width / 2;
		WindowHeight = screenSize.height / 2;
		setSize(WindowWidth * 3 / 2, WindowHeight * 3 / 2);
		this.setMinimumSize(new Dimension(200, 200));
		setLocation(WindowWidth / 4, WindowHeight / 4);

		// Create Pieces
		MainListener = new RoverGUIListener(this);
		Settings = new RoverSettings(this);
		BaseDisplay = new RoverSplitWindow(this);
		RoverSplitWindow testdisplay = new RoverSplitWindow(this);
		Data = new RoverData(this);
		
		// For Testing VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
		// set some data to display
		Data.setHealth(new RoverSysHealth());
		Data.setStatus(new RoverStatus());
		Data.setArmStatus(new RoverArmStatus());
		// End Testing ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

		// Format Pieces
		BaseDisplay.splitHorizontally();
		BaseDisplay.divideByHalf();
		
		testdisplay.splitVertically();
		testdisplay.divideByHalf();
		testdisplay.setTopComponent(new RoverVideoDisplay(this));
		testdisplay.setBottomComponent(new RoverVideoDisplay(this));
		
		BaseDisplay.setTopComponent(testdisplay);
		BaseDisplay.setBottomComponent(new RoverTabWindow(this));
		
		// Add pieces
		this.add(Settings, BorderLayout.NORTH);
		this.add(BaseDisplay, BorderLayout.CENTER);
		
		setVisible(true);
	}

	// Getters and Setters ____________________________________________________________________________________________________
	public RoverSplitWindow getBaseDisplay() {
		return BaseDisplay;
	}

	public void setBaseDisplay(RoverSplitWindow baseDisplay) {
		BaseDisplay = baseDisplay;
	}

	public RoverData getData() {
		return Data;
	}

	public void setData(RoverData data) {
		Data = data;
	}

	public RoverGUIListener getMainListener() {
		return MainListener;
	}

	public void setMainListener(RoverGUIListener mainListener) {
		MainListener = mainListener;
	}
	
	public RoverSettings getSettings() {
		return Settings;
	}
	
	public void setSettings(RoverSettings settings) {
		Settings = settings;
	}

	public int getWindowWidth() {
		return WindowWidth;
	}

	public void setWindowWidth(int windowWidth) {
		WindowWidth = windowWidth;
	}

	public int getWindowHeight() {
		return WindowHeight;
	}

	public void setWindowHeight(int windowHeight) {
		WindowHeight = windowHeight;
	}
	
}
