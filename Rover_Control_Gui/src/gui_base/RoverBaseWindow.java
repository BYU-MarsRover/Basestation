package gui_base;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Toolkit;

import gui_base.control_panel.RoverSettings;
import gui_base.current_data.RoverData;
import gui_base.displays.RoverImageDisplay;
import gui_base.formats.RoverSplitWindow;
import gui_base.formats.RoverTabWindow;

import javax.swing.JFrame;
import javax.swing.JTextArea;

import packet_models.*;

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
	private RoverSplitWindow<RoverSplitWindow<RoverImageDisplay, RoverImageDisplay>, RoverSplitWindow<RoverSplitWindow<JTextArea, JTextArea>, RoverTabWindow>> BaseDisplay;
	/* I know the previous line looks huge, but it is a template class. Rather than create 3 classes that would effectively be identical
	 * I created one general class. Unfortunately this method involves a large amount of nesting in the template class
	 * - it contains a base split with two splits within that
	 * - the left split holds two normal classes
	 * - the right split holds another split and a normal class
	 * - the final split holds two normal classes
	 */
	private RoverData Data;
//	private ClientPortal Portal;
	private int WindowWidth;
	private int WindowHeight;
	
	public RoverBaseWindow() {

		// Set Window Format
		initWindowSize();

		// Create Pieces
		initClassAttributes();
		
		// Create all the sub split windows
		RoverSplitWindow<RoverImageDisplay, RoverImageDisplay> displayA = new RoverSplitWindow<RoverImageDisplay, RoverImageDisplay>(this);
		RoverSplitWindow<RoverSplitWindow<JTextArea, JTextArea>, RoverTabWindow> displayB = new RoverSplitWindow<RoverSplitWindow<JTextArea, JTextArea>, RoverTabWindow>(this);
		RoverSplitWindow<JTextArea, JTextArea> subDisplay = new RoverSplitWindow<JTextArea, JTextArea>(this);

		// For Testing VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
		// set some data to display
		initTestData();
		// End Testing ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		
		// Format and set Pieces
		// left half of GUI
		displayA.splitVertically();
		displayA.divideByHalf();
		displayA.setComponentA(new RoverImageDisplay(this));
		displayA.setComponentB(new RoverImageDisplay(this));
		
		displayA.getComponentA().setImage("hyperion.jpg");
		
		// top right corner of GUI
		subDisplay.splitHorizontally();
		subDisplay.divideToFourth();
		subDisplay.setComponentA(new JTextArea());
		subDisplay.setComponentB(new JTextArea());
		
		subDisplay.getComponentA().append(Data.getStatus().dataToString());
		subDisplay.getComponentB().append(Data.getGPS().dataToString());
		
		// Right side of GUI
		displayB.splitVertically();
		displayB.divideByHalf();
		displayB.setComponentA(subDisplay);
		displayB.setComponentB(new RoverTabWindow(this));
		
		// GUI foundation
		BaseDisplay.splitHorizontally();
		BaseDisplay.divideByHalf();
		BaseDisplay.setComponentA(displayA);
		BaseDisplay.setComponentB(displayB);

		// Add pieces
		this.add(Settings, BorderLayout.NORTH);
		this.add(BaseDisplay, BorderLayout.CENTER);
		
		setVisible(true);
	}

	// Initialization Functions
	/**
	 * Initializes the window frame size according to the size of the screen.
	 * Sets it to be half the screen size in each direction, and places the GUI at the center of the screen.
	 */
	private void initWindowSize() {
		Toolkit kit = Toolkit.getDefaultToolkit();
		setTitle("Mars Rover Control");
		Dimension screenSize = kit.getScreenSize();
		WindowWidth = screenSize.width / 2;
		WindowHeight = screenSize.height / 2;
		setSize(WindowWidth * 3 / 2, WindowHeight * 3 / 2);
		this.setMinimumSize(new Dimension(200, 200));
		setLocation(WindowWidth / 4, WindowHeight / 4);
	}
	
	
	/**
	 * Initializes the class attributes:
	 * - Creates a GUI listener
	 * - Creates a Settings panel
	 * - Creates a display panel
	 * - Creates the data class to stored data to be displayed
	 */
	private void initClassAttributes() {
		MainListener = new RoverGUIListener(this);
		Settings = new RoverSettings(this);
		BaseDisplay = new RoverSplitWindow<RoverSplitWindow<RoverImageDisplay,RoverImageDisplay>,RoverSplitWindow<RoverSplitWindow<JTextArea, JTextArea>,RoverTabWindow>>(this);
		Data = new RoverData(this);
	}
	
	// General Functions


	// Testing Functions
	/**
	 * Sets some bogus data into the data class to be displayed
	 * Done through a test/default constructor of each type
	 */
	private void initTestData() {
		Data.setHealth(new RoverSysHealth());
		Data.setStatus(new RoverStatus());
		Data.setArmStatus(new RoverArmStatus());
		Data.setIMU(new RoverIMU());
		Data.setGPS(new RoverGPS());
	}
	
	
	// Getters and Setters ____________________________________________________________________________________________________
	public RoverSplitWindow<RoverSplitWindow<RoverImageDisplay, RoverImageDisplay>, RoverSplitWindow<RoverSplitWindow<JTextArea, JTextArea>, RoverTabWindow>> getBaseDisplay() {
		return BaseDisplay;
	}
	

	public void setBaseDisplay(RoverSplitWindow<RoverSplitWindow<RoverImageDisplay, RoverImageDisplay>, RoverSplitWindow<RoverSplitWindow<JTextArea, JTextArea>, RoverTabWindow>> baseDisplay) {
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
