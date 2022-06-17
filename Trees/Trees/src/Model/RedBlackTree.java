package Model;

public class RedBlackTree <Key extends Comparable<Key>, Value> {
    private static final boolean RED = true;
    private static final boolean BLACK = false;
    private class Node {
        boolean color;
        Node right;
        Node left;
        Key key;
        Value val;
        Integer count;

        public Node(Key key, Value val) {
            this(key, val, BLACK);
        }
        public Node(Key key, Value val, Boolean color) {
            this.key = key;
            this.val = val;
            this.color = color;
            this.right = this.left = null;
            this.count = 1;
        }
    }
    Node root;
    public RedBlackTree() {
        this.root = null;
    }
    public RedBlackTree(Key key, Value val) {
        root = new Node(key, val);
    }
    private boolean isRed(Node node) {
        return node == null ? BLACK : node.color == RED;
    }
    public int treeHeight() {
        if (root == null) return 0;
        int height = 1;
        Node current = this.root;
        while ((current.left != null) || (current.right != null)) {
            if (!isRed(current)) height++;
            current = current.right != null ? current.right : current.left;
        }
        return height;
    }

    //Assumes node has a red right link
    public Node rotateLeft (Node oldNode) {
        //Verificar se o right link saindo de node realmente é red
        assert(isRed(oldNode.right));
        Node newNode = oldNode.right;
        oldNode.right = newNode.left;
        newNode.left = oldNode;
        newNode.color = oldNode.color;
        oldNode.color = RED;
        newNode.count = oldNode.count;
        oldNode.count = 1 + size(oldNode.left) + size(oldNode.right);
        return newNode;
    }
    public Node rotateRight (Node oldNode) {
        assert(isRed(oldNode.left));
        Node newNode = oldNode.left;
        oldNode.left = newNode.right;
        newNode.right = oldNode;

        newNode.count = oldNode.count;
        newNode.color = oldNode.color;

        oldNode.count = 1 + size(oldNode.left) + size(oldNode.right);
        oldNode.color = RED;

        return newNode;
    }
    public Integer size(Node node) {
        return node == null ? 0 : node.count;
    }
    public Value get(Key key) {
        Node current = root;
        while (current != null) {
            int cmp = key.compareTo(current.key);
            if (cmp == 0) {
                return current.val;
            }
            if (cmp > 0) {
                current = current.right;
            }
            else {
                current = current.left;
            }
        }
        return null;
    }
    public void put(Key key, Value val) {
        this.root = put(key, val, root);
        root.color = BLACK;
    }
    private Node put(Key key, Value val, Node current) {
        if (current == null) {
            return new Node(key, val, RED);
        }
        int cmp = key.compareTo(current.key);
        if (cmp == 0) {
            current.val = val;
        }
        if (cmp < 0) {
            current.left = put(key, val, current.left);
        }
        else {
            current.right = put(key, val, current.right);
        }

        if (isRed(current.right) && !isRed(current.left))
            current = rotateLeft(current);

        if (isRed(current.left) && isRed(current.left.left))
            current = rotateRight(current);

        if (isRed(current.right) && isRed(current.left))
            flipColors(current);

        return current;
    }



    public void flipColors(Node node) {
        assert(isRed(node.right));
        assert(isRed(node.left));
        node.right.color = node.left.color = BLACK;
        //insert node in its parent node
        node.color = RED;
    }

}
