package Model;

public class NodeClass<Key extends Comparable<Key>, Value> {
    Key key;
    Value val;
    NodeClass left;
    NodeClass right;
    Integer count;

    public NodeClass(Key key, Value val) {
        this.key = key;
        this.val = val;
        this.left = null;
        this.right = null;
        this.count = 1;
    }
}
