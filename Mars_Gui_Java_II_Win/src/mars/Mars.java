// Filename:        Mars.java
// Creator:         Joseph DeVictoria
// Creation Date:   February 18, 2015
// Purpose:         Driver for Server/Client-emulator of Mars Rover Basestation.

package mars;

public class Mars{
    
    public static void main(String args[]){

        if (args[0].equals("-S")){
            Server marsServer =  new Server(args[1], args[2]);
            marsServer.run();
        }

        if (args[0].equals("-C")){
            Client marsClient = new Client(args[1], args[2], args[3]);
            marsClient.run();
        }
    }

    public static void printUsage(){
        System.out.println("USAGE:");
        System.out.println("SERVER: java Mars -S host port"); 
        System.out.println("CLIENT: java Mars -C host port");
    }

}
