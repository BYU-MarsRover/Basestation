package gui_base.displays;

import gui_base.RoverBaseWindow;

import javax.swing.JTextArea;

@SuppressWarnings("serial")
public class RoverTextArea extends JTextArea {

	private RoverBaseWindow Root;
	
	public RoverTextArea(RoverBaseWindow basewindow) {
		Root = basewindow;
		
		this.setEditable(false);
		this.setVisible(true);
	}

	public RoverBaseWindow getRoot() {
		return Root;
	}

	public void setRoot(RoverBaseWindow root) {
		Root = root;
	}
	
}
