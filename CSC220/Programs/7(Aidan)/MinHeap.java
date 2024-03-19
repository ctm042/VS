public class MinHeap {

    private int[] Heap;
    private int size = 0;

    // CONSTRUCTOR BAYBEE
    public MinHeap() {
        this.Heap = new int[7];
    }

//////////////////////////////////////////////////////////////////////

    // For returning the position of the parent
    private int getParent(int index) { return ((int)Math.floor(index - 1) / 2); }

    // For returning the position of the left child
    private int getLeftChild(int index) { return (2 * index) + 1; }

    // For returning the position of the right child
    private int getRightChild(int index) { return (2 * index) + 2; }

    // Other helper methods
    private boolean hasParent(int index) { return getParent(index) >= 0; }
    private boolean hasLeftChild(int index) { return getLeftChild(index) < size; }
    private boolean hasRightChild(int index) { return getRightChild(index) < size; }
    private int parent(int index) { return Heap[getParent(index)]; }
    private int leftChild(int index) { return Heap[getLeftChild(index)]; }
    private int rightChild(int index) { return Heap[getRightChild(index)]; }

    private void swap(int index1, int index2) {
        int temp = Heap[index1];
        Heap[index1] = Heap[index2];
        Heap[index2] = temp;
    }


//////////////////////////////////////////////////////////////////////

    // Insert method
    public void insert(int key) {
        Heap[this.size] = key;
        size += 1;
        minHeapifyUp();
    }

//////////////////////////////////////////////////////////////////////

    public int findMin() {
        if (size == 0) {
            return -1;
        } else {
            return Heap[0];
        }
    }

//////////////////////////////////////////////////////////////////////

    public int extractMin() {
        if (size == 0) {
            return -1;
        } else {
            int output = Heap[0];
            Heap[0] = Heap[size - 1];
            size -= 1;
            minHeapifyDown();
            return output;
        }
    }

//////////////////////////////////////////////////////////////////////

    private void minHeapifyUp() {
        int index = size - 1;
        while (hasParent(index) && parent(index) > Heap[index]) {
            swap(getParent(index), index);
            index = getParent(index);
        }
    }

//////////////////////////////////////////////////////////////////////

    private void minHeapifyDown() {
        int index = 0;
        while (hasLeftChild(index)) {
            int sIndex = getLeftChild(index);
            if (hasRightChild(index) && rightChild(index) < leftChild(index)) {
                sIndex = getRightChild(index);
            } else if (Heap[index] < Heap[sIndex]) {
                break;
            } else {
                swap(index, sIndex);
            }
            index = sIndex;
        }
    }

//////////////////////////////////////////////////////////////////////

    public boolean isEmpty() {
        if (size == 0) {
            return true;
        } else {
            return false;
        }
    }
}
