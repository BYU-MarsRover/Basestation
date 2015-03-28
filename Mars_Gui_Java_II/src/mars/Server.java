// Filename:        Server.java
// Creator:         Joseph DeVictoria
// Creation Date:   February 18, 2015
// Purpose:         Attempt at implementing the server portion of our
//                  Mars rover base station.

package mars;

import java.net.*;
import java.util.*;

public class Server{
    
    private final static int ARMPACKETSIZE = 12;
    private final static int MAINPACKETSIZE = 12;
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
                packet = new DatagramPacket(new byte[ARMPACKETSIZE], ARMPACKETSIZE);

                // Receive a packet (waits for packet to arrive).
                socket.receive(packet) ;

                // Print the packet intelligently.
                byte [] data = packet.getData();
                if (data[1] == -54) {
                    System.out.println("Arm packet:");
                    StringBuilder sb = new StringBuilder();
                    sb.append("0x");
                    for (int i = 0; i < data.length; i++) {
                        sb.append(String.format(".%X", data[i]));
                    }
                    System.out.println(sb.toString());
                }
                if (data[1] == -56) {
                    System.out.println("Main packet:");
                    StringBuilder sb = new StringBuilder();
                    sb.append("0x");
                    for (int i = 0; i < MAINPACKETSIZE; i++) {
                        sb.append(String.format(".%X", data[i]));
                    }
                    System.out.println(sb.toString());
                }
                /* Print the packet.
                System.out.println(packet.getAddress() + " " + 
                                   packet.getPort() + ": " + 
                                   data);*/

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
