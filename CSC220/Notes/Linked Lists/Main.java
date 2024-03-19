class Node {
    private char data;
    private Node next;

    // constructor
    public Node(char data) {
        this.data = data;
        next = null;
    }

    // accessors
    public char getData() {
        return data;
        }
    public Node getNext() {
        return next;
        }

    // mutators
    public void setNext(Node next) {
        this.next = next;
    }
}

class LinkedList {
    private Node head;
    private Node tail;

    // constructor
    public LinkedList() {
        head = tail = null;
    }

    public void append(char data) {
        // case 0 (0 nodes)
        if (head == null) {
            Node temp = new Node(data);
            head = temp;
            tail = temp;
        }
        // case 1 (1 or more)
        else {
            Node temp = new Node(data);
            tail.setNext(temp);
            tail = temp;
        }
    }

    public char getValueAt (int pos) {
        Node cur = head;
        int i = 0;
        while (i < pos) {
            cur = cur.getNext();
            i++;
        }
        return cur.getData();
    }

    public void printBackwards() {
        if (tail == null) {
            return;
        }
        System.out.print(tail.getData());
        if (head == tail) {
            return;
        }
        Node markedNode = tail;
        while (markedNode != head) {
            Node cur = head;
            while (cur.getNext() != markedNode) {
                cur = cur.getNext();
            }
            System.out.print(cur.getData());
            markedNode = cur;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        LinkedList llist = new LinkedList();
        llist.append('a');
        llist.append('b');
        llist.append('c');
        System.out.println(llist.getValueAt(0));
        System.out.println(llist.getValueAt(1));
        System.out.println(llist.getValueAt(2));
        llist.printBackwards();
    }   
}