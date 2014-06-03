/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author michael
 */

import org.junit.*;
import static org.junit.Assert.*;

public class TestUnit {
    @Test(timeout=30000) public void addTest()
    {
      System.out.println("This is a test");
      
      assertTrue("Code Format Unit working", testCodeFormat());
    }

    private boolean testCodeFormat() {
        String testExample = "{a = b; 35 = 7 * 5 ; *x = y->z;}" ;
        String correctExample = "{ a = b ; 35 = 7 * 5 ; x = y -> z ; }";
        
        assertNull("Null - This is bad",ClearFile.clear(testExample));
        
        return true;
    }
}
