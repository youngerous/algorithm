import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int[] arr = new int[sc.nextInt()];
        for(int i=0; i<arr.length; i++)
        	arr[i] = sc.nextInt();
        
        quickSort(arr, 0, arr.length-1);
        print(arr);
	}
	
	public static void quickSort(int[] arr, int start, int end) {
		if(start >= end)	return;
		
		int pivot = start;
		int idx = start+1;
		int jdx = end;
		int temp = 0;
		
		while(idx <= jdx) {
			while(idx <= end && arr[idx] <= arr[pivot])	idx++;
			while(jdx > start && arr[jdx] >= arr[pivot])	jdx--;
			
			if(idx > jdx) {
				temp = arr[pivot];
				arr[pivot] = arr[jdx];
				arr[jdx] = temp;
			}else {
				temp = arr[idx];
				arr[idx] = arr[jdx];
				arr[jdx] = temp;
			}
		}
		
		quickSort(arr, start,jdx-1);
		quickSort(arr, jdx+1, end);
	}
	
	
	public static void print(int[] arr) {
		for(int row=0; row<arr.length; row++) {
			System.out.print(arr[row]+" ");
		}
	}
}//end Main