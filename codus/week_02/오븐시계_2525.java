package codus.week_02;
import java.util.Scanner;

public class 오븐시계_2525 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int h = scan.nextInt();
        int m = scan.nextInt();
        int oven = scan.nextInt();
        if (m+oven < 60)
        {
            System.out.println(h + " " +(m+oven));
        }
        else
        {
            
            int a =(m+oven)/60;
            int hour = h + a;
            int b =(m+oven)%60;
            if(h + a >= 24)
            {
                hour = hour -24;
            }
            System.out.println(hour + " " + b);
        }
    }
}
