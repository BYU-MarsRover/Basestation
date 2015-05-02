// Filename:        Client.java
// Creator:         Joseph DeVictoria
// Creation Date:   February 18, 2015
// Purpose:         Attempt at implementing a client emulator for our
//                  Mars rover base station.

package mars;

import java.net.*;
import java.util.*;
import java.io.*;
import java.math.*;

public class Client{

    private final static int PACKETSIZE = 12;
    private DatagramSocket socket;
    private InetAddress hostone;
    private InetAddress hosttwo;
    private DatagramPacket packet;
    private int port;
    private Scanner input;

    public Client(String hostOneIn, String hostTwoIn, String portIn){
        try{
            // Convert the arguments first, to ensure that they are valid
            hostone = InetAddress.getByName(hostOneIn);
            hosttwo = InetAddress.getByName(hostTwoIn);
            port = Integer.parseInt(portIn);
            
            // Construct the socket
            socket = new DatagramSocket() ;

            // Create input Scanner.
            input = new Scanner(new File("..\\bin\\xbox_to_java"));
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
                while (tempData.equals("")){
					input = new Scanner(new File("..\\bin\\xbox_to_java"));
                    if (input.hasNextLine()){
                        tempData = input.nextLine();
                    }
					input.close();
                }

                BigInteger data = new BigInteger(tempData);
                byte [] data2 = data.toByteArray();

                if (data2[1] == -54) {
                    packet = new DatagramPacket(data2,data2.length,hostone,port);
                }
                else if (data2[1] == -56) {
                    packet = new DatagramPacket(data2,data2.length,hosttwo,port);
                }
                else {
                    System.out.println("No valid packet data found!!!");
                    System.exit(1);
                }

                // Send it
                socket.send(packet);
                try {
                    Thread.sleep(10);
                } catch(InterruptedException ex) {
                    Thread.currentThread().interrupt();
                }
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

