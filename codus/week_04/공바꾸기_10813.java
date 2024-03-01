package codus.week_04;

import java.util.Scanner;

public class 공바꾸기_10813 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int M = scan.nextInt();
        int []arr = new int[N];
        for(int i = 0; i<N; i++)
        {
            arr[i] = i+1;
        }

        for(int i=0; i<M; i++)
        {
            int a = scan.nextInt() ;
            int b = scan.nextInt() ;
            int x =0 ;
            x = arr[a-1];
            arr[a-1] = arr[b-1];
            arr[b-1] = x;
        }
        for(int i=0; i<N; i++)
        {
            System.out.print(arr[i]+" ");
        }
        
    }
}