import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int total = sc.nextInt();
		int cnt = 0;
		
		for(int j = 0; j < total; j++) {
			int test_case = sc.nextInt();
			if(isPrime(test_case)) cnt++;
		}
		
		System.out.println(cnt);
	}//end main
	
	public static boolean isPrime(int num) {
		if(num < 2)    return false;
		
		for(int i = 2; i*i <= num; i++)
			if(num % i == 0)    return false;
		
		return true;
	}	
}//end Main