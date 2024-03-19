public class Main {
    public static void main(String[] args){

        // Making first set
        int min1 = 0;
        int max1 = 150;
        int quant1 = 20;

        int[] originalset1 = new int[quant1];
        for (int i = 0; i < originalset1.length; i++) originalset1[i] = (int)(Math.random() * ((max1+1) - min1) + min1);

        int[] setcopy1 = originalset1.clone();
        int[] setcopy2 = originalset1.clone();
        int[] setcopy3 = originalset1.clone();
        int[] setcopy4 = originalset1.clone();

        CocktailSort cocktail = new CocktailSort();
        QuickSort quick = new QuickSort();
        CountingSort counting = new CountingSort();
        CombSort comb = new CombSort();

        // Printing first set
        System.out.println("TESTING with n = " + originalset1.length);

        System.out.print("  Original List:   ");
        for (int i = 0; i < originalset1.length; i++) {System.out.print(originalset1[i] + " ");}
        System.out.println();

        cocktail.cocktailSort(setcopy1);
        System.out.print("  Cocktail sorted: ");
        cocktail.print(setcopy1);

        quick.quickSort(setcopy2);
        System.out.print("  Quick sorted:    ");
        quick.print(setcopy2);

        counting.countingSort(setcopy3);
        System.out.print("  Counting sorted: ");
        counting.print(setcopy3);

        comb.combSort(setcopy4);
        System.out.print("  Comb sorted      ");
        comb.print(setcopy4);

        // Making second set
        int min2 = 0;
        int max2 = 150;
        int quant2 = 20000;

        int[] originalset2 = new int[quant2];
        for (int i = 0; i < originalset2.length; i++) originalset2[i] = (int)(Math.random() * ((max2+1) - min2) + min2);

        int[] setcopy5 = originalset2.clone();
        int[] setcopy6 = originalset2.clone();
        int[] setcopy7 = originalset2.clone();
        int[] setcopy8 = originalset2.clone();

        long start;
        long end;

        // Printing second set
        System.out.println("\nTIMING with n = " + originalset2.length);

        start = System.nanoTime();
        cocktail.cocktailSort(setcopy5);
        end = System.nanoTime();
        System.out.println("  Cocktail took " + Math.round((end-start)/10000)/100.00 + " ms");
        // 371.13,     365.21,     577.03,     531.28,     442.98,     471.96,     503.61,     444.64,     502.04,     447.09
        // 465.697 avg
        
        start = System.nanoTime();
        quick.quickSort(setcopy6);
        end = System.nanoTime();
        System.out.println("  Quick took    " + Math.round((end-start)/10000)/100.00 + " ms");
        // 2.38        2.96,       5.81,       3.59,       7.13,       7.35,       5.24,       2.77,       2.69,       3.12
        // 4.304 avg

        start = System.nanoTime();
        counting.countingSort(setcopy7);
        end = System.nanoTime();
        System.out.println("  Counting took " + Math.round((end-start)/10000)/100.00 + " ms");
        // 0.87        1.39,       1.74,       1.52,       1.49,       1.35,       1.78,       1.61,       1.21,       1.67
        // 1.463 avg

        start = System.nanoTime();
        comb.combSort(setcopy8);
        end = System.nanoTime();
        System.out.println("  Comb took     " + Math.round((end-start)/10000)/100.00 + " ms");
        // 4.67,       4.83,       5.16,       10.78,      5.68,       5.48,       4.86,       7.45,       5.5,        7.14
        // 6.155 avg
    }
}

class CocktailSort{
    public void cocktailSort(int[] set){
        int n = set.length;

        for (int i = 1; i < (n - 1); i++){
            //forward direction
            boolean anySwapsMade = false;
            for (int j = i; j < (n - 1); j++){
                if (set[j] < set[j-1]){
                    swap(set, j, j-1);
                    anySwapsMade = true;
                }
            }
            if (!anySwapsMade) {break;}

            // backwards direction
            anySwapsMade = false;
            for (int j = (n - 1); j > (i - 1); j--){
                if (set[j] < set[j-1]){
                    swap(set, j, j-1);
                    anySwapsMade = true;
                }
            }
            if (!anySwapsMade) {break;}
        }
    }

    private void swap(int[] arr, int i, int j) {int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;}
    public void print(int[] set) {for (int i = 0; i < set.length; i++) {System.out.print(set[i] + " ");}System.out.println();}
}

class QuickSort{
    public void quickSort(int[] list){quickSort(list, 0, list.length-1);}
    private void quickSort(int[] list, int left, int right){
        if (left < right){
            int p = partition(list, left, right);
            quickSort(list, left, p-1);
            quickSort(list, p+1, right);
        }
    }

    private int partition(int[] list, int left, int right){
        int pivotPos = left;
        left++;
        while (true){
            while ((left < list.length) && (list[left] < list[pivotPos])) {left++;}
            while ((right >= 0) && (list[right] > list[pivotPos])) {right--;}
            if (left >= right) break;
            else {
                swap(list, left, right);
                left++;
                right--;
            }
        }
        swap(list, right, pivotPos);
        return right;
    }

    private void swap(int[] arr, int i, int j) {int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;}
    public void print(int[] set) {for (int i = 0; i < set.length; i++) {System.out.print(set[i] + " ");}System.out.println();}
 }
 
class CountingSort{
    public void countingSort(int[] set){
        int n = set.length;

        // allocate count array and initialize to all zeros
        int max = set[0];
        for (int i = 1; i < n; i++) if (set[i] > max) max = set[i];
        int count[] = new int[max+1];

        // calculate the histogram of key frequencies
        for (int i = 0; i < n; i++) count[set[i]]++;

        // calculate the starting index for each key
        int total = 0;
        for (int i = 0; i < count.length; i++) {
            int oldCount = count[i];
            count[i] = total;
            total += oldCount;
        } 

        // allolate output array
        int[] output = new int[n];

        // copy to output array, keeping order of inputs with equal keys (aka stable sort)
        for (int i = 0; i < n; i++){
            int value = set[i];
            output[count[value]] = value;
            count[value] = count[value]+1;
        }
        
        for (int i = 0; i < n; i++) set[i] = output[i];
    }

    public void print(int[] set) {for (int i = 0; i < set.length; i++) {System.out.print(set[i] + " ");}System.out.println();}
}

class CombSort{
    public void combSort(int[] set){
        int n = set.length;
        int gap = n;
        boolean anySwapsMade = true;
        // break conditions : swap = false or gap = 1
                              
        while (!(!anySwapsMade || gap == 1)){
            anySwapsMade = false;
            gap = (((gap*10)/13) < 1) ? 1 : (gap*10)/13;
            for (int i = 0; i < (n - gap); i++){
                if (set[i] > set[i+gap]) {
                    swap(set, i, i+gap);
                    anySwapsMade = true;
                }
            }
        }
    }

    private void swap(int[] arr, int i, int j) {int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;}
    public void print(int[] set) {for (int i = 0; i < set.length; i++) {System.out.print(set[i] + " ");}System.out.println();}
}
