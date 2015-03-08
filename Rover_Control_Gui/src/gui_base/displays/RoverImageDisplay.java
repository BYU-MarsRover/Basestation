package gui_base.displays;

import java.awt.Image;
import java.awt.image.BufferedImage;

import gui_base.RoverBaseWindow;

import javax.swing.JPanel;

@SuppressWarnings("serial")
public class RoverImageDisplay extends JPanel {
	
	private RoverBaseWindow Root;
	private static Image NULL_IMAGE = new BufferedImage(10, 10, BufferedImage.TYPE_INT_ARGB);
	
	/**
	 * Default Constructor
	 * 
	 * @param root
	 */
	public RoverImageDisplay(RoverBaseWindow root) {
		Root = root;
//		Shapes = new ArrayList<DrawingShape>();
		
//		Scale = 1.0;
//		w_originX = 500;
//		w_originY = 150;
//		initDrag();
		
//		this.setBackground(new Color(178, 223, 210));
//		this.setPreferredSize(new Dimension(Root.getMyWidth(), Root.getMyHeight() * 3 / 8));
//		this.setMinimumSize(new Dimension(200, 200));
//		this.setMaximumSize(new Dimension(1000, 1000));
		
//		this.addMouseListener(mouseAdapter);
//		this.addMouseMotionListener(mouseAdapter);
//		this.addMouseWheelListener(mouseAdapter);
		
	}

	public RoverBaseWindow getRoot() {
		return Root;
	}

	public void setRoot(RoverBaseWindow root) {
		Root = root;
	}

	public static Image getNULL_IMAGE() {
		return NULL_IMAGE;
	}

	public static void setNULL_IMAGE(Image nULL_IMAGE) {
		NULL_IMAGE = nULL_IMAGE;
	}
	
}
