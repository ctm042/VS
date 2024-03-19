import java.util.*;

import javax.lang.model.util.ElementScanner14;

class SortAndSearch{
    public static void main(String[] args){
        // setup
        // create array of 15 random integers
        int[] myArray = new int[15];
        Random r = new Random(); // generate random numbers
        Scanner s = new Scanner(System.in); // get user input

        // populate the array with random numbers between 0 and 99
        for(int i = 0; i < myArray.length; i++)
            myArray[i] = r.nextInt(99);

        // call the other methods
        printArray(myArray);
        sortArray(myArray);
        printArray(myArray);

        int num = s.nextInt(); // get a number to search for
        int index = searchArray(myArray, num); // search through the array for the nmuber

        if(index == -1)
            System.out.println("Value not found");
        else
            System.out.println("Value found at index" + index);

    }
    //print the array
    public static void printArray(int[] arr){
        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i] + " ");
        }
    }
    //sort the array using selection sort
    public static void sortArray(int[] arr){
        for(int i = 0; i < arr.length - 1; i++){
            // assum first value is the min
            int min = i;
            // look for a new min
            for(int j = i + 1; i < arr.length; j++){
                if(arr[j] < arr[min]){
                    min = j;
                }
            }
        
            //swap
            int temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    }
    // search through the array using binary search
    public static int searchArray(int[] arr, int value){
        int first = 0;
        int last = arr.length - 1;

        while(first <= last){
            // find middle value
            int mid = (first + last)/2;
            
            // if value is in the middle fo the array, return its index
            if(value == arr[mid])
                return mid;

            // else
            else if(value > arr[mid])
                first = mid + 1;
            else
                last = mid -1;
        }
        // otherwise value not found
        return -1;
    }
}