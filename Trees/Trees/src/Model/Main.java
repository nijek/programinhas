package Model;

import java.util.Random;

public class Main {
    public static void main(String[] args) {

        Random rand = new Random();
        BinarySearchTree bt = new BinarySearchTree();
        int max = 10;
        int[] nums = new int[max];
//        for (int i = 0; i < max; i++) {
//            nums[i] = rand.nextInt(max);
//        }
        nums = new int[]{0, 30, 90, 70, 50, 20, 40, 10, 80, 60};

        System.out.println("Começou");
        for (int i = 0; i < 1000; ++i) {
            bt.put(nums[i%10], nums[i%10]);
        }
        bt.put(30, 40);
//        System.out.println("Já foi");
//        for (int i = 0; i < max; i++) {
//            bt.get(i);
//            System.out.println((bt.count(i)));
//        }

        System.out.println(bt.min());
        System.out.println(bt.max());

        System.out.println(bt.floor(15));
        System.out.println(bt.ceiling(-15));

        System.out.println(bt.size());
    }
}
