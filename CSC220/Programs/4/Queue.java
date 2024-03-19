/** Queue abstract data type */
public class Queue<T> {
  /** List objects to hold our queue items.
      Use List operations to implement the methods below */
  private List<T> list;
  
  public Queue() {
    // instantiate list here
    list = new List<T>();
  }
  
  /**
   * Adds an element to the end of the queue
   * @param value
   */
  public void enqueue(T value) {
    list.append(value);
  }
  
  /**
   * Look at and remove the first element from the queue
   * @return <T>
   */
  public T dequeue() {
    T c = list.getValueAt(0);
    list.deleteAt(0);
    return c;
  }

  /**
   * Look at but do not remove the first element from the queue
   * @return <T>
   */
  public T front() {
    return list.getValueAt(0);
  }

  /**
   * Checks for elements in the queue.
   * @return boolean
   */
  public boolean isEmpty() {
    if (list.size()==0){return true;}
    return false;
  }
}
