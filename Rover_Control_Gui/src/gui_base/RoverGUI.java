package gui_base;

import java.awt.EventQueue;

import javax.swing.JFrame;

/** Rover GUI application
 * This is the starting point for the Rover GUI application. It contains the main() 
 * function. Conventions for the programming are as follows:
 *   1. Packages will have words separated by the underscore character. ( my_package )
 *   2. Classes will begin with the Rover key word. (RoverNewClass) 
 *   3. Classes will begin with Capitol letters. (Rover)
 *   4. Classes will have words separated by Capitalization. ( RoverMyClass )
 *   5. 
 * 
 * This class will get the basic application started, and then will open a welcome dialog
 * window. Then open the primary application will run.
 * 
 * @author Nathan Warner
 *
 */
public class RoverGUI {
	
	public RoverGUI() {
		
	}
	
	public static void main(String[] args) {
		// Host and Port are examples from my RecordIndexer
		//final String Host = args[0];
		//final int Port = Integer.parseInt(args[1]); 
		
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				
				new RoverWelcomeDialog();
				RoverBaseWindow baseWindow = new RoverBaseWindow();
				baseWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
				
			}
		});	// END EventQueue
		
	}	// END main
	
}
