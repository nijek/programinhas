package Model;

public class BinarySearchTree <Key extends Comparable<Key>, Value> {
   private class Node {
       Key key;
       Value val;
       Node left;
       Node right;
       Integer count;
       public Node(Key key, Value val) {
           this.key = key;
           this.val = val;
           this.left = this.right = null;
           this.count = 1;
       }
   }
    Node root;
    public BinarySearchTree(Key key, Value val) {
        root = new Node(key, val);
    }
    public BinarySearchTree() {
        root = null;
    }

    public Value get(Key key) {
       Node node = getNode(key);
        if (node == null) {
            return null;
        }
        return node.val;
    }
    public Node getNode(Key key) {
       Node current = root;
        while (current != null) {
            int compare = (key).compareTo(current.key);
            if (compare == 0) {
                return current;
            }
            if (compare < 0) {
                current = current.left;
            }
            else {
                current = current.right;
            }
        }
        System.out.println("No such key");
        return null;
    }
    public void put(Key key, Value val) {
        root = put(key, val, root);
    }
    private Node put(Key key, Value val, Node current) {
        if (current == null) {

            return new Node(key, val);
        }
        int compare = (key).compareTo(current.key);

        if (compare < 0) {
            current.left = put(key, val, current.left);
        }
        else if (compare > 0) {
            current.right = put(key, val, current.right);
        }
        else {
            current.val = val;
        }
        current.count = 1 + size(current.left) + size(current.right);
        return current;
    }
    public Integer count(Key key) {
       Node node = getNode(key);
        if (node == null) {
            return 0;
        }
        return node.count;
    }
    public Integer size(Node node) {
        if (node == null) {
            return 0;
        }
        return node.count;
    }
    public Integer size() {
        return size(root);
    }
    public Key min() {
        if (root == null) {
            return null;
        }
       Node current = root;
        while(current.left != null) {
            current = current.left;
        }
        return current.key;
    }
    public Key max() {
        if (root == null) {
            return null;
        }
       Node current = root;
        while(current.right != null) {
            current = current.right;
        }
        return current.key;
    }
    public Key floor(Key key) {
        if (root == null) {
            return null;
        }

       Node current = root;
        Key floor = null;

        while (current != null) {
            int cmp = key.compareTo(current.key);
            if (cmp == 0) {
                return current.key;
            }
            if (cmp > 0) {
                floor = current.key;
                current = current.right;
            }
            else {
                current = current.left;
            }
        }
        return floor;
    }
    public Key ceiling(Key key){
        if (root == null) {
            return null;
        }
       Node current = root;
        Key ceiling = null;

        while (current != null) {
            int cmp = key.compareTo(current.key);
            if (cmp == 0) {
                return current.key;
            }
            if (cmp > 0) {
                current = current.right;
            }
            else {
                ceiling = current.key;
                current = current.left;
            }
        }
        return ceiling;
    }
}

