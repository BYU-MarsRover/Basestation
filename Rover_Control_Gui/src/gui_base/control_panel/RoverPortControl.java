package gui_base.control_panel;

import java.awt.GridLayout;

import gui_base.RoverBaseWindow;

import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

@SuppressWarnings("serial")
public class RoverPortControl extends JPanel {
	
	private RoverBaseWindow Root;
	private JLabel PortName;
	private JLabel HostName;
	private JTextField Port;
	private JTextField Host;
	
	public RoverPortControl(RoverBaseWindow basewindow) {
		// create attributes
		Root = basewindow;
		PortName = new JLabel("Port: ");
		HostName = new JLabel("Host: ");
		Port = new JTextField();
		Host = new JTextField();
		
		// customize attributes
		
		// place attributes
		this.setLayout(new GridLayout());
		this.add(PortName);
		this.add(Port);
		this.add(HostName);
		this.add(Host);
		
		setVisible(true);
	}



	public RoverBaseWindow getRoot() {
		return Root;
	}



	public void setRoot(RoverBaseWindow root) {
		Root = root;
	}



	public JTextField getPort() {
		return Port;
	}



	public void setPort(JTextField port) {
		Port = port;
	}



	public JTextField getIPAddress() {
		return Host;
	}



	public void setIPAddress(JTextField iPAddress) {
		Host = iPAddress;
	}
	
}
