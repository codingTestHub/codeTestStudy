package codus.week_05;

import java.util.Scanner;

public class 바구니뒤집기_10811 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int M = scan.nextInt();
        int [] arr = new int[N];

        for(int i=0; i<N; i++)
        {
            arr[i] = i+1;
        }

        for(int i=0; i<M; i++)
        {
            int a = scan.nextInt()-1;
            int b = scan.nextInt()-1;

            while (a < b) {
                int temp = arr[a];
                arr[a++] = arr[b];
                arr[b--] = temp;
            }
        }


        for(int i =0; i<N; i++)
        {
            System.out.print(arr[i] + " ");
        }
    }

}
