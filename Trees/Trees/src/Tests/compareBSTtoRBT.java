package Tests;

import Model.BinarySearchTree;
import Model.RedBlackTree;
import org.junit.Before;
import org.junit.jupiter.api.Test;

import java.util.Random;

public class compareBSTtoRBT {
    BinarySearchTree bt;
    RedBlackTree rbt;
    Random rand;

    @Before
    public void setUp() {
        bt = new BinarySearchTree<>();
        rbt = new RedBlackTree<>();
        rand = new Random();
    }
    @Test
    public void tests() {
        for(int i = 0; i < 10000000; i++) {

        }
    }
}
