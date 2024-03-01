package codus.week_04;

import java.util.Scanner;

public class 최댓값_2562 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int [] a = new int[9];
        int max = 0;
        int num = 0;
        for(int i =0; i<9; i++) {
            a[i] = scan.nextInt();
            if(max < a[i])
            {
                max = a[i];
                num = i+1;
            }
        }
        System.out.println(max);
        System.out.println(num);
    }
}
