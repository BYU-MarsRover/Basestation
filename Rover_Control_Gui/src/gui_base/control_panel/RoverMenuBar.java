package gui_base.control_panel;

import java.awt.event.ActionListener;

import gui_base.RoverBaseWindow;

import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.SwingConstants;

@SuppressWarnings("serial")
public class RoverMenuBar extends JMenuBar {
	private RoverBaseWindow Root;
	private JMenu FileDropMenu;
	private JMenu SettingsDropMenu;
	private JMenu HelpDropMenu;
	
	public RoverMenuBar(RoverBaseWindow root) {
		Root = root;
		FileDropMenu = new JMenu("File");
		SettingsDropMenu = new JMenu("Settings");
		HelpDropMenu = new JMenu("Help");
		
		this.add(FileDropMenu);
		this.add(SettingsDropMenu);
		this.add(HelpDropMenu);
		
		
		// add items to File drop menu (add in reverse order of how you want them displayed)
		addMenuItem(FileDropMenu, "Exit", Root.getMainListener().getCommandListener());
		addMenuItem(FileDropMenu, "TempOption_2", Root.getMainListener().getCommandListener());
		addMenuItem(FileDropMenu, "TempOption_1", Root.getMainListener().getCommandListener());
		
		// add items to Settings drop menu (add in reverse order of how you want them displayed)
		addMenuItem(SettingsDropMenu, "Restore Defaults", Root.getMainListener().getCommandListener());
		addMenuItem(SettingsDropMenu, "Preferences", Root.getMainListener().getCommandListener());
		addMenuItem(SettingsDropMenu, "Size", Root.getMainListener().getCommandListener());
		
		// add items to Help drop menu (add in reverse order of how you want them displayed)
		addMenuItem(HelpDropMenu, "Info", Root.getMainListener().getCommandListener());
		addMenuItem(HelpDropMenu, "Test", Root.getMainListener().getCommandListener());
		
		
		this.setVisible(true);
	}


	public void addMenuItem(JMenu menu, String label, ActionListener listener) {
		JMenuItem option = new JMenuItem(label);
		option.addActionListener(listener);
		menu.add(option, SwingConstants.CENTER);
	}
	
}
