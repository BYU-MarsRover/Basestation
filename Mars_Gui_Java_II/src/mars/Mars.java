// Filename:        Mars.java
// Creator:         Joseph DeVictoria
// Creation Date:   February 18, 2015
// Purpose:         Driver for Server/Client-emulator of Mars Rover Basestation.

package mars;

public class Mars{
    
    public static void main(String args[]){
        // Check arguments for matching usage cases.
        /*if ((args.length != 3) || (args[0] != "-S")){
            if (args[0] != "-C"){
                printUsage();
                return;
            }
        }*/

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
