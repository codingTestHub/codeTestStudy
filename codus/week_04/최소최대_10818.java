package codus.week_04;

import java.util.Scanner;

public class 최소최대_10818 {
    public static void main(String[] args) {
        
       
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int[] num = new int[a];
        int b = scan.nextInt();
        int max=b,min=b;
        

        for(int i=1; i<a; i++)
        {
            
            num[i] = scan.nextInt();
            if (max<num[i])
            {
                max = num[i];
            }
            if(min>num[i])
            {
                min = num[i];
            }
        }
        System.out.println(min +" "+max);
    }

}