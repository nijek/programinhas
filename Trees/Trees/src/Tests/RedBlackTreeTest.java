package Tests;
import Model.BinarySearchTree;
import org.junit.Before;
import Model.RedBlackTree;
import org.junit.Test;

import java.util.Date;
import java.util.Random;


import static org.junit.jupiter.api.Assertions.assertEquals;

public class RedBlackTreeTest {
    int MAX = 10000000;
    RedBlackTree rbt;
    Random rand;
    @Before
    public void setUp() {
    rbt = new RedBlackTree();
    rand = new Random();
    }

    @Test
    public void createRedBlackTreeWithStrings() {
        int max = MAX;
        String[] stringTestCase = new String[max];
        for (int i = 0; i < max; i++) {
            String s = rand.toString() + rand.nextLong();
            stringTestCase[i] = s;
            rbt.put(s, s);
            if (i % 5000 == 0) System.out.println("i: " + i + " h: " + rbt.treeHeight());
        }

        for(String s : stringTestCase) {
            assertEquals(s, rbt.get(s));
        }
    }
    @Test
    public void RedBlackTreeOrderedInsertion(){
        int max = 10*MAX;
        for (int i = 0; i < max; i++) {
            rbt.put(i,i);
            if (i % 5000 == 0) System.out.println("i: " + i + " h: " + rbt.treeHeight());

        }
        for (int i = 0; i < max; i++) {
            if (i % 5000 == 0) System.out.println("i volta: " + i + " h: " + rbt.treeHeight());
            assertEquals(i, rbt.get(i));
        }
    }
    @Test
    public void createRedBlackTreeWithDateObject(){
        int max = MAX;
        long[] dates = new long[max];
        for (int i = 0; i < max; i++) {
            dates[i] = rand.nextLong();
            rbt.put(new Date(dates[i]), new Date (dates[i]));
            if (i % 5000 == 0) System.out.println("i: " + i + " h: " + rbt.treeHeight());

        }
        for (int i = 0; i < max; i++) {
            Date date = new Date(dates[i]);
            assertEquals(date, rbt.get(date));
        }
    }
}
