package gui_base;

import javax.swing.JOptionPane;

/** Welcome dialog
 * This is a basic welcome pop-up. Useful for testing start up, and just kind of nice.
 * not really necessary but simple enough.
 * 
 * @author Nathan Warner
 *
 */

@SuppressWarnings("serial")
public class RoverWelcomeDialog extends JOptionPane {
	
	private String Message;
	
	public RoverWelcomeDialog() {
		Message = "Welcome to Houstan Mobile Control!\n";
		JOptionPane.showMessageDialog(getParent(), Message, "Welcome", JOptionPane.PLAIN_MESSAGE);
		setVisible(true);
	}
	
}
