import java.util.*;
public class Main {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);

        int[][] arr = new int[8][2];

        for (int i = 0; i < 8; i++) {
            arr[i][0] = i;
            arr[i][1] = sc.nextInt();
        }

        Arrays.sort(arr, (o1,o2) -> {
            return o1[1]-o2[1];
        });

        int sum = 0;
        int[] sort_arr = new int[5];

        for (int i = 3; i < 8; i++) {
            sum += arr[i][1];
            sort_arr[i-3] = arr[i][0];
        }

        Arrays.sort(sort_arr);
        System.out.println(sum);
        for (int i=0; i < 5; i++) {
            System.out.print(sort_arr[i]+1 + " ");
        }
    }
}