public class BST {
    public Node root;

    // constructor
    public BST() {
        root = null;
    }
  
    // methods
    /**
     * Inserts value into the Binary Search Tree
     * @param value
     */
    public void insert(int value){
        Node temp = new Node(value);

        Node cur = root;
        Node prev = null;
        if (root==null){
            root = temp;
        }

        while (cur != null){
            prev = cur;
            if (value < cur.getData()){
                cur = cur.getLeft();
                if (cur==null){
                    prev.setLeft(temp);
                }
            }
            else {
                cur = cur.getRight();
                if (cur==null){
                    prev.setRight(temp);
                }
            }
        }
    }

    /**
     * Searches for given value in the Binary Search Tree. Returns true if found.
     * @param value
     * @return
     */
    public boolean search(int value){
        Node cur = root;
        while (cur != null){
            if (cur.getData()==value){return true;}
            else if (value < cur.getData()){cur = cur.getLeft();}
            else {cur = cur.getRight();}
        }
        return false;
    }

    // public void delete(int value){
    //     Node cur = root;
    //     Node prev = null;
    //     int direction = -1;

    //     while (cur != null){
    //         prev = cur;

    //         // found value
    //         if (cur.getData()==value){
                

    //             // mark with new node
    //             Node mark = cur;
    //             int sucdirection = -1;

    //             // check 1 to the right
    //             if (cur.getRight() != null){
    //                 prev = cur;
    //                 cur = cur.getRight();
    //                 sucdirection = 1;
    //             }

    //             // then check leftmost
    //             while (cur.getLeft() != null){
    //                 prev = cur;
    //                 cur = cur.getLeft();
    //                 sucdirection = 0;
    //             }
                
    //             // cur at successor. set mark to cur's data
    //             mark.setData(cur.getData());

    //             // delete cur (delete its pointer)
    //             if (sucdirection == 0){prev.setLeft(null);}
    //             else if (sucdirection == 1){prev.setRight(null);}

    //             // sucdirection is -1 and cur is at mark (at a leaf)
    //             else if (direction == 0){prev.setLeft(null);}
    //             else if (direction == 1){prev.setRight(null);}
    //         }

    //         // value less than node
    //         else if (value < cur.getData()){
    //             cur = cur.getLeft();
    //             direction = 0;
    //         }

    //         // value greater than node
    //         else {
    //             cur = cur.getRight();
    //             direction = 1;
    //         }
    //     }
    // }

    /////////////////////////////////////////

    // void delete(int value) { root = deleteRec(root, value); }
    // Node deleteRec(Node root, int value)
    // {
    //     // Base Case: If the tree is empty
    //     if (root == null){return root;}
  
    //     // Otherwise, recur down the tree
    //     if (value < root.getData()){root.setLeft(deleteRec(root.getLeft(), value));}
    //     else if (value > root.getData()){root.setRight(deleteRec(root.getRight(), value));}
  
    //     // if value is same as root's value, then this is the node to be deleted
    //     else {
    //         // node with only one child or no child
    //         if (root.getLeft() == null){return root.getRight();}
    //         else if (root.getRight() == null){return root.getLeft();}
  
    //         // node with two children: Get the successor
    //         int minv = root.getData();
    //         while (root.getLeft() != null) {
    //             minv = root.getLeft().getData();
    //             root = root.getLeft();
    //         }
    //         root.setData(minv);

    //         // Delete the inorder successor
    //         root.setRight(deleteRec(root.getRight(), root.getData()));
    //     }
    //     return root;
    // }
  
    //////////////////////////////////////////////

    // Function to delete a node from a BST
    // public void delete(int value){
    //     // return if the key is not found in the tree
    //     if (search(value)==false || root==null){return;}
    //     Node prev = null;
    //     Node cur = root;
    //     while (cur != null){
            
    //         if (cur.getData()==value){
    //             // Case 1: node to be deleted has no children (leaf)
    //             if (cur.getLeft()==null && cur.getRight()==null){
                    
    //             }

    //             // Case 2: node to be deleted has children (parent)
    //             if (cur.getLeft()!=null || cur.getRight()!=null){
    //                 Node mark = cur;
    //                 prev = cur;
    //                 cur = cur.getRight();
    //                 while (cur.getLeft()!=null){
    //                     prev = cur;
    //                     cur = cur.getLeft();
    //                 }
    //                 mark.setData(cur.getData());
    //                 if (prev.getData()>cur.getData()) prev.setLeft(cur.getLeft());
    //                 else if (prev.getData()<cur.getData()) prev.setRight(cur.getLeft());
    //             }
            
    
    //             // Case 3: node to be deleted has only one child
    //             if (cur.getLeft()!=null && cur.getRight()=null){ // only left
    //                 if (prev.getData()>cur.getData()) prev.setLeft(cur.getLeft());
    //                 else if (prev.getData()<cur.getData()) prev.setRight(cur.getLeft());
    //                 else System.out.println("Error [0]");
    //             }
    //             else if (cur.getLeft()=null && cur.getRight()!=null){ // only right
    //                 if (prev.getData()>cur.getData()) prev.setLeft(cur.getLeft());
    //                 else if (prev.getData()<cur.getData()) prev.setRight(cur.getLeft());
    //                 else System.out.println("Error [1]");
    //             }
            

    //         }
    //         else if (value < cur.getData()){cur = cur.getLeft();}
    //         else {cur = cur.getRight();}
    //         prev = cur;
    //     }
    // }

    ///////////////////////////////////////

    public void delete(int data) {deleteNode(root, data);}
    private Node deleteNode(Node root, int data) {
        if (root == null) return root;
        if (data < root.getData()) {root.setLeft(deleteNode(root.getLeft(), data));} 
        else if (data > root.getData()) {root.setRight(deleteNode(root.getRight(), data));} 
        else {
            // node with no leaf nodes
            if (root.getLeft() == null && root.getRight() == null) {return null;} 

            // node with one node (no left node)
            else if (root.getLeft() == null) {return root.getRight();} 

            // node with one node (no right node)
            else if (root.getRight() == null) { return root.getLeft();} 

            // nodes with two nodes
            // search for min number in right sub tree
            else {
                int minValue = minValue(root.getRight());
                root.setData(minValue);
                root.setRight(deleteNode(root.getRight(), minValue));
            }
        }
        return root;
    }

    private int minValue(Node node) {
        if (node.getLeft() != null) {return minValue(node.getLeft());}
        return node.getData();
    }

    /**
     * Returns the smallest (leftmost) element.
     * @return
     */
    public int min(){
        if (root==null){return -1;}
        Node cur = root;
        while (cur.getLeft() != null){
            cur = cur.getLeft();
        }
        return cur.getData();
    }

    /**
     * Returns the largest (rightmost) element.
     * @return
     */
    public int max(){
        if (root==null){return -1;}
        Node cur = root;
        while (cur.getRight() != null){
            cur = cur.getRight();
        }
        return cur.getData();
    }

    /**
     * Returns the Binary Search Tree in an ordered string.
     * @return
     */
    public String inorder(){ return inorder(root);}
    private String inorder(Node the){
        if (the==null){return "";}
        String result = inorder(the.getLeft()) + the.getData() + " " + inorder(the.getRight());
        return result;
    }

    /**
     * Returns the Binary Search Tree in a preordered string.
     * @return
     */
    public String preorder(){return preorder(root);}
    private String preorder(Node the){
        if (the==null){return "";}
        String result = the.getData() + " " + preorder(the.getLeft()) + preorder(the.getRight());
        return result;
    }

    /**
     * Returns the Binary Search Tree in a postordered string.
     * @return
     */
    public String postorder(){return postorder(root);}
    private String postorder(Node the){
        if (the==null){return "";}
        String result = postorder(the.getLeft()) + postorder(the.getRight()) + the.getData() + " ";
        return result;
    }
}
