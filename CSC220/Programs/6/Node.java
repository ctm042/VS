public class Node {
    // put all fields from Node class here
    private int data;
    private Node left;
    private Node right;
    
    // put all methods from Node class here
    // constructor
    public Node(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
  
    // accessors
    public int getData() {return data;}
    public Node getLeft() {return left;}
    public Node getRight() {return right;}
  
    // mutators
    public void setData(int data) {this.data = data;}
    public void setLeft(Node left) {this.left = left;}
    public void setRight(Node right) {this.right = right;}
  }