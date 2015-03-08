package gui_base;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/** GUI Listener class
 * The purpose of this class is to hold all the listeners for buttons, menu items,
 * mouse clicks etc.  They have been consolidated into a single class so that it won't
 * be necessary to silence all other listeners when syncing all the panels after a ping.
 * 
 * It is intended that this will be passed in to the BaseWindow class, and most other lower
 * panels and then the specific listener (contained within this class) can be pulled out and
 * used as an input to individual action options such as buttons, dropmenu's, etc.
 * 
 * @author Nathan Warner
 *
 */
public class RoverGUIListener {

	private RoverBaseWindow Root;
	private ActionListener RoverCommand;
	
	private String TestString;
	
	public RoverGUIListener(RoverBaseWindow baseWindow) {
		Root = baseWindow;
		RoverCommand = new CommandAction();
		TestString = "TestSuccess";
	}
	
	// menu handlers ____________________________________________________________________________________________________
	private void fileExit() {
		Root.dispose();
	}
	
	private void fileOption1() {
		System.out.println("Option 1 under construction");
	}
	
	private void fileOption2() {
		System.out.println("Option 2 under construction");
	}
	
	private void settingsSize() {
		System.out.println("Size settings under construction");
	}
	
	private void settingsPreferences() {
		System.out.println("Preferences settings under construction");
	}
	
	private void settingsRestoreDefaults() {
		System.out.println("Restore Defaults under construction");
	}
	
	private void helpInfo() {
		System.out.println("See RoverGUI file for programming conventions");
	}
	
	// Action Listeners ____________________________________________________________________________________________________
	private class CommandAction implements ActionListener {
		
		public void actionPerformed(ActionEvent event) {
			
			String command = event.getActionCommand();
			
			if(command.equals("TempOption_1")) {
				fileOption1();
			} else if(command.equals("TempOption_2")) {
				fileOption2();
			} else if(command.equals("Exit")) {
				fileExit();
			} else if(command.equals("Size")) {
				settingsSize();
			} else if(command.equals("Preferences")) {
				settingsPreferences();
			} else if(command.equals("Restore Defaults")) {
				settingsRestoreDefaults();
			} else if(command.equals("Info")) {
				helpInfo();
			} else {
				// false alarm
			}
			
		}
		
	}
	
	// Getters and Setter ____________________________________________________________________________________________________
	
	public void setBaseWindow(RoverBaseWindow window) {
		Root = window;
	}
	
	public ActionListener getCommandListener() {
		return RoverCommand;
	}
	
	public String getTestString() {
		return TestString;
	}
	
}
