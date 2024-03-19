/** Linked List implementation of our List abstract data type */
public class List<T> {
	// put all fields from ListAsLinkedList class here
	private Node head;
	private Node tail;
	private int size;
  
	// put all methods from ListAsLinkedList class here
	// constructor
	public List() {
    head = tail = null;
	size = 0;
	}

	/**
	 * Creates a new node that is appended to tail node.
	 * @param data
	 */
	public void append(T data) {
		Node<T> temp = new Node<T>(data);
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

	/**
	 * Creates a new node that is prepended to the head node.
	 * @param data
	 */
	public void prepend(T data) {
		Node<T> temp = new Node<T>(data);
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

	/**
	 * Deletes the node at index given
	 * @param pos
	 */
	public void deleteAt(int pos){
		// case where pos = head
		if (pos==0){
			head=head.getNext();
			size--;
			return;
		}
		Node cur = head;
		for (int i = 0; i < pos-1; i++){
			cur = cur.getNext();
		}
		cur.setNext(cur.getNext().getNext());
		size--;
	}

	/**
	 * Returns the amount of elements in the list.
	 * @return int
	 */
	public int size(){
		return size;
	}

	/**
	 * Returns the element at the given index
	 * @param pos
	 * @return <T>
	 */
	public T getValueAt(int pos){
		Node<T> cur = head;
		for (int i = 0; i < pos; i++){cur = cur.getNext();}
        return cur.getData();
	}

	/**
	 * Returns the index of the first apperance of the given element
	 * @param value
	 * @return int
	 */
	public int positionOf(T value){
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
}

/** A linked list node for our linked list */
class Node<T> {
  // put all fields from Node class here
  private T data;
  private Node next;
  
  // put all methods from Node class here
  // constructor
  public Node(T data) {
      this.data = data;
      this.next = null;
  }

  // accessors
  public T getData() {return data;}
  public Node getNext() {return next;}

  // mutators
  public void setNext(Node next) {this.next = next;}
  
}
