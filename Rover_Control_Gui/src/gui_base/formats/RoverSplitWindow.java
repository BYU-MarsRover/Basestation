package gui_base.formats;

import javax.swing.JSplitPane;

import gui_base.RoverBaseWindow;
import gui_base.displays.RoverImageDisplay;
import gui_base.displays.RoverVideoDisplay;

@SuppressWarnings("serial")
public class RoverSplitWindow extends JSplitPane {

	private RoverBaseWindow Root;
	private RoverImageDisplay LeftView;
	private RoverVideoDisplay RightView;
	
	public RoverSplitWindow(RoverBaseWindow baseWindow) {
		Root = baseWindow;
		
		//this.setOrientation(HORIZONTAL_SPLIT);
//		this.setDividerLocation(Root.getWindowWidth() * 3 / 4);
		
		LeftView = new RoverImageDisplay(Root);
		RightView = new RoverVideoDisplay(Root);
		
//		this.setTopComponent(LeftView);
//		this.setBottomComponent(RightView);
		
	}

	// Auxiliary ________________________________________________________________________________
	public void splitVertically() {
		this.setOrientation(VERTICAL_SPLIT);
	}
	
	public void splitHorizontally() {
		this.setOrientation(HORIZONTAL_SPLIT);
	}
	
	public void divideByHalf() {
		if(this.getOrientation() == VERTICAL_SPLIT) {
			this.setDividerLocation(Root.getWidth() / 4);	
		} else {
			this.setDividerLocation(Root.getHeight() * 3 / 4);
		}
	}
	
	// Getters and Setters ________________________________________________________________________________
	public RoverBaseWindow getRoot() {
		return Root;
	}

	public void setRoot(RoverBaseWindow root) {
		Root = root;
	}

	public RoverImageDisplay getLeftView() {
		return LeftView;
	}

	public void setLeftView(RoverImageDisplay leftView) {
		LeftView = leftView;
	}

	public RoverVideoDisplay getRightView() {
		return RightView;
	}

	public void setRightView(RoverVideoDisplay rightView) {
		RightView = rightView;
	}
	
	
}
