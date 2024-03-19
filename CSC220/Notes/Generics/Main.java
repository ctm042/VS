class Node<T> {
    private T data;
    private Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }

    public T getData() {return data;}

    public Node<T> getNext() {return next;}
    public void setNext(Node<T> next) {this.next = next;}
}

class LinkedList<T> {
    private Node<T> head;
    private Node<T> tail;

    //constructor
    public LinkedList() {
        head = tail = null;
    }

    public void append(T data) {
        Node<T> temp = new Node<>(data);
        if (head == null){
            head = temp;
        }
        else {
            tail.setNext(temp);
        }
        tail = temp;
    }
    public void printAll(){
        Node<T> walker = head;
        while(walker != null){
            System.out.println(walker.getData() + " ");
            walker = walker.getNext();
        }
        System.out.println();
    }
}

class Car {
    private int numTires;
    
    public Car(int numTires){
        this.numTires = numTires;
    }

    public String toString() {
        return "this is a car with " + numTires + " tires.";
    }
}

public class Main{
    public static void main(String[] args){
        LinkedList<Car> linkedList = new LinkedList<>();
        linkedList.append(new Car(3));
        linkedList.append(new Car(4));
        linkedList.append(new Car(6));
        linkedList.printAll();
    }
}