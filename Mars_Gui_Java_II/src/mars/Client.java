// Filename:        Client.java
// Creator:         Joseph DeVictoria
// Creation Date:   February 18, 2015
// Purpose:         Attempt at implementing a client emulator for our
//                  Mars rover base station.

package mars;

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

