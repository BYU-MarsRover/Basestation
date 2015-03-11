package gui_base.displays;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.geom.Rectangle2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

import gui_base.RoverBaseWindow;

import javax.imageio.ImageIO;
import javax.swing.JPanel;

@SuppressWarnings("serial")
public class RoverImageDisplay extends JPanel {

	private RoverBaseWindow Root;
	private static Image NULL_IMAGE = new BufferedImage(10, 10, BufferedImage.TYPE_INT_ARGB);
	private ArrayList<DrawingShape> Shapes; 

	/**
	 * Default Constructor
	 * 
	 * @param root
	 */
	public RoverImageDisplay(RoverBaseWindow root) {
		Root = root;
		Shapes = new ArrayList<DrawingShape>();

		this.setBackground(new Color(178, 223, 210));
		this.setPreferredSize(new Dimension(Root.getWidth(), Root.getHeight() * 3 / 8));
		this.setMinimumSize(new Dimension(200, 200));
		this.setMaximumSize(new Dimension(1000, 1000));

//		Image hyperion = loadImage("hyperion.jpg");
//		Shapes.add(new DrawingImage(hyperion, new Rectangle2D.Double(0, 0, hyperion.getWidth(null), hyperion.getHeight(null))));

		this.setVisible(true);
	}

	// Functions
	public void setImage(String imagePath) {
		Shapes.clear();
		Image image = loadImage(imagePath);
		Shapes.add(new DrawingImage(image, new Rectangle2D.Double(0, 0, image.getWidth(null), image.getHeight(null))));
		this.repaint();
	}
	
	private Image loadImage(String imageFile) {
		try {
			return ImageIO.read(new File(imageFile));
		}
		catch (IOException e) {
			return NULL_IMAGE;
		}
	}
	
	@Override
	protected void paintComponent(Graphics g) {

		super.paintComponent(g);
		
		Graphics2D g2 = (Graphics2D)g;
		drawBackground(g2);
		drawShapes(g2);
	}
	
	private void drawBackground(Graphics2D g2) {
		g2.setColor(getBackground());
		g2.fillRect(0,  0, getWidth(), getHeight());
	}

	private void drawShapes(Graphics2D g2) {
		for (DrawingShape shape : Shapes) {
			shape.draw(g2);
		}
	}

	// Other
	interface DrawingShape {
		void draw(Graphics2D g2);
//		boolean contains(Graphics2D g2, double x, double y);
//		void adjustPosition(double dx, double dy);
	}

	class DrawingImage implements DrawingShape {

		private Image image;
		private Rectangle2D rect;
		
		public DrawingImage(Image image, Rectangle2D rect) {
			this.image = image;
			this.rect = rect;
		}

		@Override
		public void draw(Graphics2D g2) {
			Rectangle2D bounds = rect.getBounds2D();
			g2.drawImage(image, (int)bounds.getMinX(), (int)bounds.getMinY(), (int)bounds.getMaxX(), (int)bounds.getMaxY(),
							0, 0, image.getWidth(null), image.getHeight(null), null);
		}	
	}

	// Getters & Setters
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
