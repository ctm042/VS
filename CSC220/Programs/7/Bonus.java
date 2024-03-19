public class Bonus {
    public static void main(String[] args) {
        MinHeap heap = new MinHeap();
        heap.insert(8);
        heap.insert(1);
        heap.insert(7);
        heap.insert(6);
        heap.insert(3);
        
        heap.decreaseKey(4, 0);
        heap.increaseKey(0, 9);
        heap.decreaseKey(2, 5);
        heap.decreaseKey(2, 0);
        heap.increaseKey(3, 10);
        heap.increaseKey(1, 11);
        
        System.out.print("Numbers in sorted order: ");
        while(!heap.isEmpty()) {
            System.out.print(heap.extractMin() + " ");
        }
        System.out.println();
    }
}