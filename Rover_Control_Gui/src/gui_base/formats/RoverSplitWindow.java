package gui_base.formats;

import java.awt.Component;

import javax.swing.JSplitPane;

import gui_base.RoverBaseWindow;

@SuppressWarnings("serial")
public class RoverSplitWindow<RoverTypeA, RoverTypeB> extends JSplitPane {

	private RoverBaseWindow Root;
	private RoverTypeA ComponentA;
	private RoverTypeB ComponentB;
	
	// Constructors
	public RoverSplitWindow(RoverBaseWindow baseWindow) {
		Root = baseWindow;		
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
	
	public void divideToFourth() {
		if(this.getOrientation() == VERTICAL_SPLIT) {
			this.setDividerLocation(Root.getWidth() / 2);	
		} else {
			this.setDividerLocation(Root.getHeight() / 2);
		}
	}
	
	// Getters & Setters ________________________________________________________________________________
	public RoverBaseWindow getRoot() {
		return Root;
	}

	public void setRoot(RoverBaseWindow root) {
		Root = root;
	}
	

	public RoverTypeA getComponentA() {
		return ComponentA;
	}
	

	public void setComponentA(RoverTypeA componentA) {
		ComponentA = componentA;
		this.setTopComponent((Component) ComponentA);
	}
	

	public RoverTypeB getComponentB() {
		return ComponentB;
	}
	

	public void setComponentB(RoverTypeB componentB) {
		ComponentB = componentB;
		this.setBottomComponent((Component) ComponentB);
	}
	
}
