import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int ee = sc.nextInt()-1;
		int ss = sc.nextInt()-1;
		int mm = sc.nextInt()-1;
		
		for(int i=0; ; i++) {
			if(i%15==ee && i%28==ss && i%19==mm) {
				System.out.println(i+1);
				break;
			}
		}
	}
	
}//end Main