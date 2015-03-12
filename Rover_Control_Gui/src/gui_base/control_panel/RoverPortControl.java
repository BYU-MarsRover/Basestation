package gui_base.control_panel;

import java.awt.GridLayout;
import java.awt.event.ActionListener;

import gui_base.RoverBaseWindow;

import javax.swing.JButton;
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
	
	// Constructors
	public RoverPortControl(RoverBaseWindow basewindow) {
		// create attributes
		Root = basewindow;
		PortName = new JLabel("Port: ");
		HostName = new JLabel("Host: ");
		Port = new JTextField();
		Host = new JTextField();
		
		// customize attributes if needed
		
		// place attributes
		this.setLayout(new GridLayout());
		this.add(PortName);
		this.add(Port);
		this.add(HostName);
		this.add(Host);
		addTextField();				// currently not nessecary
		addButton("Connect", Root.getMainListener().getCommandListener());
		
		setVisible(true);
	}

	// Functions
	/**
	 * Adds a button to the control layout. Includes setting button title and listener.
	 * A handler for the listener will still need to be implemented in the RoverGUIListener for this button.
	 * @param label		- the title or name seen on the button
	 * @param listener	- the listener object that will be monitoring for pressing of the button
	 */
	private void addButton(String label, ActionListener listener) {
		JButton button = new JButton(label);
		button.addActionListener(listener);
		this.add(button);
	}
	
	/**
	 * This is temporary. If I need to add a text listener to the specific text field then I will use this to add
	 * the text fields. That way I can default easily to the main GUI listener.
	 */
	private void addTextField() {
		
	}
	
	// Getters & Setters
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
