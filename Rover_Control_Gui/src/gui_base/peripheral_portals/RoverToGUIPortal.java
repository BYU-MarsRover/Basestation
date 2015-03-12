package gui_base.peripheral_portals;

import java.net.*;

public class RoverToGUIPortal {

	private final static int PACKETSIZE = 100 ;

	private int Port;
	private int Host;
	private DatagramSocket Socket;
	private DatagramPacket Packet;

	// Constructors
	public RoverToGUIPortal(int host, int port) {
		Port = port;
		Host = host;
		try {
			Socket = new DatagramSocket(Port);
		} catch (Exception e) {
			System.out.println(e);
		}
	}

	public RoverToGUIPortal(String host, String port) {
		Port = Integer.parseInt(port);
		Host = Integer.parseInt(host);
		try {
			Socket = new DatagramSocket(Port);
		} catch (Exception e) {
			System.out.println(e);
		}
	}

	// Other
	public void run(){
		try{
			System.out.println("Mars Rover Server listening on port: " + Port + ", & host: " + Host);
			while(true){
				// Create a packet.
				Packet = new DatagramPacket(new byte[PACKETSIZE], PACKETSIZE);

				// Receive a packet (waits for packet to arrive).
				Socket.receive(Packet);

				// Print the packet.
				System.out.println(Packet.getAddress() + " " + 
						Packet.getPort() + ": " + 
						new String(Packet.getData()));

				// Return the packet to the sender
				Socket.send(Packet);
			}  
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
	}
}


/*
 *  
 *
import java.net.*;
import java.util.*;
import java.io.*;

public class Client{

	private final static int PACKETSIZE = 100 ;
	private DatagramSocket socket;
	private InetAddress host;
	private DatagramPacket packet;
	private int port;
	private Scanner input;

	public Client(String hostIn, String portIn){
		try{
			// Convert the arguments first, to ensure that they are valid
			host = InetAddress.getByName(hostIn);
			port = Integer.parseInt(portIn);

			// Construct the socket
			socket = new DatagramSocket() ;

			// Create input Scanner.
			input = new Scanner(new File("/home/joseph/xbox_to_java"));
		}
		catch (Exception e){
			System.out.println(e);
		}
	}

	public void run(){
		try{
			while(true){
				// Construct the datagram packet
				String tempData = "";
				input = new Scanner(new File("/home/joseph/xbox_to_java"));
				while (tempData.equals("")){
					if (input.hasNextLine()){
						tempData = input.nextLine();
						input.close();
					}
				}
				//System.out.println("Sending: " + tempData);
				byte [] data = tempData.getBytes() ;
				packet = new DatagramPacket(data,data.length,host,port);

				// Send it
				socket.send(packet);

				// Set a receive timeout, 2000 milliseconds
				socket.setSoTimeout(2000);

				// Prepare the packet for receive
				packet.setData(new byte[PACKETSIZE]);

				// Wait for a response from the server
				socket.receive(packet);

				// Print the response
				//System.out.println("Received: " + new String(packet.getData()));
			}
		}
		catch( Exception e ){
			System.out.println(e);
		}
		finally{
			if(socket != null)
				socket.close() ;
		}
	}
}

public class Server{

	private final static int PACKETSIZE = 100 ;
	private DatagramSocket socket;
	private DatagramPacket packet;
	private int port;

	public Server(String hostIn, String portIn){
		try{
			// Convert the argument to ensure that is it valid
			port = Integer.parseInt(portIn) ;
			// Construct the socket
			socket = new DatagramSocket(port) ;
		}
		catch (Exception e){
			System.out.println(e);
		}
	}

	public void run(){
		try{
			System.out.println("Mars Rover Server listening on port " + port);
			while(true){
				// Create a packet.
				packet = new DatagramPacket(new byte[PACKETSIZE], PACKETSIZE);

				// Receive a packet (waits for packet to arrive).
				socket.receive(packet) ;

				// Print the packet.
				System.out.println(packet.getAddress() + " " + 
						packet.getPort() + ": " + 
						new String(packet.getData()));

				// Return the packet to the sender
				socket.send(packet) ;
			}  
		}
		catch(Exception e)
		{
			System.out.println(e) ;
		}
	}
} 
*
*/