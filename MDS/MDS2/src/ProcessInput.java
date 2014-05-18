
import java.awt.event.ActionEvent;
import javax.swing.JTextField;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author mihai_000
 */
class ProcessInput {
    String file;
    
    public void actionPerformed(ActionEvent evt , JTextField textField) {
        String text = textField.getText();
        System.out.println(text);
    }
}
