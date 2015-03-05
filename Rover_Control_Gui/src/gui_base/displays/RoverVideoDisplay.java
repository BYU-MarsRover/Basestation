package gui_base.displays;

import gui_base.RoverBaseWindow;

import javax.swing.JPanel;

/**	Video display panel
 * This class is meant to contain a live video feed and display it. I am not sure
 * yet if there is a library for this already, or if we will be displaying still
 * images and updated every couple fractions of a second to create a video feed.
 * 
 * @author Nathan Warner
 *
 */
@SuppressWarnings("serial")
public class RoverVideoDisplay extends JPanel {

	private RoverBaseWindow Root;
	
	public RoverVideoDisplay (RoverBaseWindow baseWindow) {
		Root = baseWindow;
	}

	// Getters & Setters ____________________________________________________________________________________________________
	public RoverBaseWindow getRoot() {
		return Root;
	}

	public void setRoot(RoverBaseWindow root) {
		Root = root;
	}
	
}
