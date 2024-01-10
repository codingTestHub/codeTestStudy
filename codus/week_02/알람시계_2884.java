package codus.week_02;

import java.util.Scanner;

public class 알람시계_2884 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        if (b < 45)
        {
            if ( a == 0)
            {
                a = 24;
            }
            a = a-1;
            b = 60 -(45-b);
        }
        else
        {
            b = b-45;
        }
        System.out.println(a + " " + b);

    }
}
