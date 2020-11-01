import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int[] arr = {sc.nextInt(), sc.nextInt(), sc.nextInt()};
        
        int min = 0;
        int index = 0;
        for(int ii=0; ii<arr.length; ii++){
            min = 1000001;
            for(int jj=ii; jj<arr.length; jj++){
                if(min > arr[jj]){
                    min = arr[jj];
                    index = jj;
                }
            }
            int temp = arr[ii];
            arr[ii] = arr[index];
            arr[index] = temp;
        }
        
        for(int idx=0; idx<arr.length; idx++){
            System.out.print(arr[idx]+" ");
        }
	}
	
}//end Main