// Filename:        MarsController.java
// Creator:         Joseph DeVictoria
// Creation Date:   March 4, 2015
// Purpose:         Attempt at implementing an xbox controller.

package mars;

import java.util.*;
import net.java.games.input.Component;
import net.java.games.input.Component.Identifier;
import net.java.games.input.Controller;
import net.java.games.input.ControllerEnvironment;

public class MarsController {
    private ArrayList<Controller> foundControllers;
    
    public static void main(String args[]) {
        MarsController newC = new MarsController();
        newC.run();
    }

    public void run(){
        System.out.println("Cool");
        System.out.println(foundControllers.toString());
    }

    public MarsController() {
        foundControllers = new ArrayList<Controller>();
        searchForControllers();
        if (!foundControllers.isEmpty()){
            System.out.println("Found controllers!");
            return;
        } 
        else {
            System.out.println("No controllers found...");
        }
    }

    public void searchForControllers() {
        Controller[] controllers = ControllerEnvironment.getDefaultEnvironment().getControllers();
        for (int i = 0; i < controllers.length; i++) {
            Controller controller = controllers[i];
            if (controller.getType() == Controller.Type.STICK ||
                controller.getType() == Controller.Type.GAMEPAD ||
                controller.getType() == Controller.Type.WHEEL ||
                controller.getType() == Controller.Type.FINGERSTICK) {
                foundControllers.add(controller);
            }
        }
    }
}
