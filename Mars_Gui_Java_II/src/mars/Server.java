// Filename:        Server.java
// Creator:         Joseph DeVictoria
// Creation Date:   February 18, 2015
// Purpose:         Attempt at implementing the server portion of our
//                  Mars rover base station.

package mars;

import java.net.*;

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
