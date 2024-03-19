public class Main {
    public static void main(String[] args){
        // instantiate our BST object
        BST tree = new BST();
        // load it up with some initial values
        tree.insert(10);
        tree.insert(5);
        tree.insert(2);
        tree.insert(1);
        tree.insert(3);
        tree.insert(8);
        tree.insert(7);
        tree.insert(9);
        tree.insert(15);
        tree.insert(12);
        tree.insert(11);
        tree.insert(13);
        tree.insert(18);
        tree.insert(17);
        tree.insert(19);

        
        // are you on Windows?
        Vis.runOnWindows = true; // set to true if running on Windows
        // test it out
        Vis.test(tree);

    }
}
