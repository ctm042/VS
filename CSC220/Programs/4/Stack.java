/** Stack abstract data type */
public class Stack<T> {
  /** List objects to hold our stack items.
      Use List operations to implement the methods below */
  private List<T> list;

  public Stack() {
    // instantiate list here
    list = new List<T>();
  }

  /**
   * Adds an element to the top of the stack
   * @param value
   */
  public void push(T value) {
    list.append(value);
  }

  /**
   * Look at and remove the top element from the top of the stack
   * @return <T>
   */
  public T pop() {
    T c = list.getValueAt(list.size()-1);
    list.deleteAt(list.size()-1);
    return c;
  }

  /**
   * Look at but do not remove the top element from the stack
   * @return <T>
   */
  public T peek() {
    return list.getValueAt(list.size()-1);
  }

  /**
   * Checks for elements in the stack.
   * @return boolean
   */
  public boolean isEmpty() {
    if (list.size()==0){return true;}
    return false;
  }
}
