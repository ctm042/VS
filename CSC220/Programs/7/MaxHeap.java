import java.lang.Math;

public class MaxHeap {
    private int heapSize;
    private int[] heap;
    private int size;
    
    public MaxHeap(){
        this.heapSize = 7;
        this.heap = new int[heapSize];
        this.size = 0;
    }

    /**
     * Adds a new key to the heap, maintaining the max heap property by 
     * calling the proper version of maxHeapify.
     * @param key
     */
    public void insert(int key){
        size++;
        heap[size-1] = key;
        if (size > 1) maxHeapifyUp(size-1);
    }

    /**
     * Returns the maximum key in the heap, but does not remove it.
     * @return Max value [int]
     */
    public int findMax(){
        if (size==0) {return -1;}
        return heap[0];
    }

    /**
     * Returns the maximum key in the heap, and removes it from the heap, 
     * maintaining the max heap property by calling the proper version of maxHeapify.
     * @return Max value [int]
     */
    public int extractMax(){
        if (size==0) {return -1;}
        int value = heap[0];
        heap[0] = heap[size-1];
        size--;
        if (size > 1) {maxHeapifyDown(0);}
        return value;
    }

    /**
     * Scans the heap, fixing violations of the max heap property.
     * @param index
     */
    public void maxHeapifyUp(int index){maxHeapifyUpRec(index);}
    private void maxHeapifyUpRec(int index){
        if (!((heap[index] < heap[getParent(index)]) || (index == 0))){
            swap(index,getParent(index));
            maxHeapifyUpRec(getParent(index));
        }
    }

    /**
     * Scans the heap, fixing violations of the max heap property.
     * @param index
     */
    public void maxHeapifyDown(int index){maxHeapifyDownRec(index);}
    private void maxHeapifyDownRec(int index){
        int max = index;
        if (hasLeft(index) && heap[getLeft(index)] > heap[max]) {max = getLeft(index);}
        if (hasRight(index) && heap[getRight(index)] > heap[max]) {max = getRight(index);}
        if (max != index) {swap(index,max); maxHeapifyDownRec(max);}
    }

    /**
     * Returns true if the heap has no keys in it, false otherwise.
     * @return boolean
     */
    public boolean isEmpty(){
        if (size==0) return true;
        return false;
    }

    /**
     * Changes the key of the node at position pos with the value of newKey. 
     * New key must be higher than the current key in that node.
     * @param index
     * @param key
     */
    public void increaseKey(int index, int key){
        heap[index] = key;
        maxHeapifyUp(index);
    }

    /**
     * Changes the key of the node at position pos with the value of newKey. 
     * New key must be lower than the current key in that node.
     * @param index
     * @param key
     */
    public void decreaseKey(int index, int key){
        heap[index] = key;
        maxHeapifyDown(index);
    }

    // Helper functions
    private int getParent(int index){return ((int)Math.floor(index - 1) / 2);}
    private int getLeft(int index){return 2 * index + 1;}
    private int getRight(int index){return 2 * index + 2;}
    private boolean hasLeft(int index){return getLeft(index)<size;}
    private boolean hasRight(int index){return getRight(index)<size;}
    private void swap(int a, int b){
        int temp=heap[a];
        heap[a]=heap[b];
        heap[b]=temp;
    }

    public void print(){
        System.out.println("");
        for (int i = 0; i < size; i++){System.out.print(heap[i] + " ");}
    }
}
