import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int target = sc.nextInt();
		int[] arr = new int[num];
		
		for(int idx = 0; idx < num; idx++) 
			arr[num-idx-1] = sc.nextInt(); 
		
		int count = 0;
		int rest = target;
		
		for(int jdx = 0; jdx < num; jdx++) {
			count += rest / arr[jdx];
			rest %= arr[jdx];
		}
		
		System.out.println(count);
		
        
	}
}