public class MyMain {
    public static void main(String[] args){
        MinHeap heap = new MinHeap();
        System.out.println("");
        heap.insert(5);heap.print();
        heap.insert(3);heap.print();
        heap.insert(2);heap.print();
        heap.insert(1);heap.print();
        heap.insert(8);heap.print();
        heap.insert(4);heap.print();

        System.out.println("");
        heap.extractMin();heap.print();
    }
}
