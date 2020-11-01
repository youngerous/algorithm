import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int people = sc.nextInt();
        int arr[] = new int[people];
        // 값 초기화
        for(int idx = 0; idx < people; idx++)
            arr[idx] = sc.nextInt();
        
        // 낮은 숫자 순으로 정렬
        int temp;
        for(int idx = 0; idx < people; idx++){
            for(int jdx = 0; jdx < people-idx-1; jdx++){
                if(arr[jdx] > arr[jdx+1]){
                    temp = arr[jdx];
                    arr[jdx] = arr[jdx+1];
                    arr[jdx+1] = temp;
                }
            }
        }
        
        // 시간 최솟값 구하기
        int time = 0;
        for(int idx = 0; idx < people; idx++){
            time += sum(arr, idx);
        }
        System.out.println(time);
    }
    
    public static int sum(int[] arr, int idx){
        int sum = 0;
        for(int jdx = 0; jdx <= idx; jdx++){
            sum += arr[jdx];
        }
        return sum;
    }
}