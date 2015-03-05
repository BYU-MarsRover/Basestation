package gui_base.control_panel;

import java.awt.BorderLayout;

import gui_base.RoverBaseWindow;

import javax.swing.JPanel;

@SuppressWarnings("serial")
public class RoverSettings extends JPanel {

	private RoverBaseWindow Root;
	public RoverMenuBar Menubar;
	public RoverPortControl Ports;
	
	public RoverSettings(RoverBaseWindow basewindow) {
		Root = basewindow;
		Menubar = new RoverMenuBar(Root);
		Ports = new RoverPortControl(Root);
		
		this.setLayout(new BorderLayout());
		this.add(Menubar, BorderLayout.NORTH);
		this.add(Ports, BorderLayout.CENTER);
		
		setVisible(true);
	}
	
}
