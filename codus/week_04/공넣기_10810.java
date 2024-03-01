package codus.week_04;

import java.util.Scanner;

public class 공넣기_10810 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int M = scan.nextInt();
        int [] num = new int[N];
        
        for(int i=0; i<M; i++)
        {
            int a = scan.nextInt();
            int b = scan.nextInt();
            int c = scan.nextInt();
            for ( int j=a-1; j<=b-1; j++)
            {
                num[j] = c;
            }
        }
        for(int i=0; i<N; i++)
        {
            System.out.print(num[i]+" ");
        }
    }
}
