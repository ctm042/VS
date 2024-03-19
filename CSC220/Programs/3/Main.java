/**
 * Name: Caleb Matherne
 * Date: 9/29/2022
 * Description: The List Abstract Data Type
 */

/** The interface for our List (Abstract Data Type) */
interface IList {
	/** Adds the given value to the end of the list */
	void append(char value);
	
	/** Adds the given value to the beginning of the list */
	void prepend(char value);
	
	/** Deletes the container at the given position (a container holds a value) */
	void deleteAt(int position);
	
	/** Returns the number of values currently in our list */
	int size();

	/** Retrieves the value at the given position (0-based) */
	char getValueAt(int position);

	/** Searches for the FIRST occurence of a given value in our list.
		* If found, it returns the position of that value.
		* If not found, it returns -1 */
	int positionOf(char value);
}


/** Array implementation of our List */
class ListAsArray implements IList {
	// initialize array to a size of 30 elements
	// this will prevent the need to resize our array

	/** Character array that keeps stores the given characters */
	private char[] array;

	/** Integer that represents the next available index in the array */
	private int tail;

	// constructor
	public ListAsArray(){
		array = new char[30];
		tail = 0;
	}
	
	public void append(char value) {
		array[tail] = value;
		tail++;

		//System.out.println("[A] Appended " + value);System.out.println(this);
	}

	public void prepend(char value) {
		for (int i = array.length -1; i > 0 ; i--) {
			array[i] = array[i - 1];
		}
		array[0] = value;
		tail++;

		//System.out.println("[A] Prepended " + value);System.out.println(this);
	}

	public void deleteAt(int position){
		char x = array[position];
		for (int i = position; i < array.length - 1; i++) {
			array[i] = array[i + 1];
		}
		tail--;

		//System.out.println("[A] Deleted " + x + " at " + position);System.out.println(this);
	}

	public int size(){
		return tail;
	}

	public char getValueAt(int position){
		return array[position];
	}

	public int positionOf(char value){
		for(int i = 0 ; i < array.length ; i++) {
			if (array[i] == value){
				return i;
			}
		}
		return -1;
	}

	// Only used for debug stuff.
	public String toString(){
		String result = "";
		for (char i : array){
			result += String.valueOf(i);
		}
		result += "\n";
		return result;
	}
}


/** Singly Linked List implementation of our List */
class ListAsLinkedList implements IList {

	private Node head;
    private Node tail;
	private int size;

    // constructor
    public ListAsLinkedList() {
        head = tail = null;
		size = 0;
    }

	public void append(char data) {
		Node temp = new Node(data);
        if (head == null){
            head = temp;
        }
        else {
            tail.setNext(temp);
        }
        tail = temp;
		size++;

		//System.out.println("[L] Appended " + data);this.printForwards();
	}

	public void prepend(char data) {
		Node temp = new Node(data);
		if (head == null) {
			head = temp;
		}
		else {
			temp.setNext(head);
		}
		head = temp;
		size++;

		//System.out.println("[L] Prepended " + data);this.printForwards();
	}

	public void deleteAt(int pos){
		Node cur = head;
		int i = 0;
		while (i < pos) {
			cur = cur.getNext();
			i++;
		}

		//System.out.println("[L] Deleted " + cur.getNext().getData() + " at " + pos);this.printForwards();

		cur.setNext(cur.getNext().getNext());
		size--;
	}

	public int size(){
		return size;
		
	}

	public char getValueAt(int pos){
		Node cur = head;
        int i = 0;
        while (i < pos) {
            cur = cur.getNext();
            i++;
        }
        return cur.getData();
	}

	public int positionOf(char value){
		Node cur = head;
        int i = 0;
        while (i < size) {
            cur = cur.getNext();
			if(cur.getData()==value){
				return i;
			}
            i++;
        }
		return -1;
	}

	// Only used for debug stuff
	public void printForwards() {
		if (tail == null) {
            return;
        }
		System.out.print(head.getData());
        if (head == tail) {
			System.out.println("\n");
            return;
        }
		Node cur = head;
		while (cur != tail) { 
			cur =cur.getNext();
            System.out.print(cur.getData());
        }
		System.out.println("\n");
	}
}


/** A singly linked list node for our singly linked list */
class Node {
	private char data;
    private Node next;

    // constructor
    public Node(char data) {
        this.data = data;
        next = null;
    }

    // accessors
    public char getData() {return data;}
    public Node getNext() {return next;}

    // mutators
    public void setNext(Node next) {this.next = next;}
}


/** contains our entry point */
public class Main {
	/** entry point - DO NOT CHANGE the pre-existing code below */
	public static void main(String[] args) {
		int[] numbers = {105,116,112,115,65,58,47,47,116,105,110,121,88,117,114,108,46,99,111,109,47};
		int[] numbers2 = {97,59,111,53,33,111,106,42,50};
		int[] numbers3 = {116,104,32,111,116,32,111,71};
		
		
		/// List as an Array
		IList array = new ListAsArray();
		
		// add values
		for(int num : numbers) {
			array.append((char)num);
		}
		for(int num : numbers3) {
			array.prepend((char)num);
		}
		
		// delete some values
		int position;
		
		position = array.positionOf((char)105);
		array.deleteAt(position);
		
		position = array.positionOf((char)65);
		array.deleteAt(position);
		
		position = array.positionOf((char)88);
		array.deleteAt(position);
	 
		// print em
		position = 0;
		while (position < array.size()) {
			System.out.print(array.getValueAt(position));
			position++;
		}
		
		
		/// List as a Linked List
		IList linkedList = new ListAsLinkedList();
		
		// add values
		for(int num : numbers2) {
			linkedList.append((char)num);
		}
		linkedList.prepend((char)55);
		linkedList.prepend((char)121);

		// delete some values
		position = linkedList.positionOf((char)59);
		linkedList.deleteAt(position);
		
		position = linkedList.positionOf((char)33);
		linkedList.deleteAt(position);
		
		position = linkedList.positionOf((char)42);
		linkedList.deleteAt(position);
		
		// print em
		position = 0;
		while (position < linkedList.size()) {
			System.out.print(linkedList.getValueAt(position));
			position++;
		}
		
		System.out.println();
		
		/**
		 * 37.9
		 * *2
		 * 75.8 (75)
		 * %10
		 * 5
		*/
		System.out.println(((int)((37.9)*2))%10);

		// ???
	}
}
