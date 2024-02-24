package codus.week_03;

import java.util.Scanner;

public class 영수증_25304 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int all_price = scan.nextInt();
        int count = scan.nextInt();
        int sum =0;
        for(int i=0; i<count; i++)
        {
            int a = scan.nextInt();
            int b = scan.nextInt();
            sum = sum+a*b;
        }
        if(all_price == sum)
        {
            System.out.println("Yes");
        }
        else
        {
            System.out.println("No");
        }
    }
}
