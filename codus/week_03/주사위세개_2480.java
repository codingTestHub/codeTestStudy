package codus.week_03;

import java.util.Scanner;

public class 주사위세개_2480 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();

        if(a==b)
        {
            if(a==c)
            {
                System.out.println(10000+a*1000);
            }
            else
            {
                System.out.println(1000+a*100);
            }
        }
        else if(a==c)
        {
            if(a==b)
            {
                System.out.println(10000+a*1000);
            }
            else
            {
                System.out.println(1000+a*100);
            }

        }
        else if(b==c)
        {
            if(a==b)
            {
                System.out.println(10000+a*1000);
            }
            else
            {
                System.out.println(1000+b*100);
            }

        }
        else
        {
            int d = a>b ? a :b;
            if(d>c)
                System.out.println(d*100);
            else
                System.out.println(c*100);
        }
    }
}
