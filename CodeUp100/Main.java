import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        char ch = sc.next().charAt(0);
        sc.close();
            
        System.out.print("hello");    //1001
        System.out.print("Hello World");    //1002
        System.out.print("Hello\nWorld");    //1003
        System.out.print("\'Hello\'");    //1004
        System.out.print("\"Hello World\"");    //1005
        System.out.print("\"!@#$%^&*()\"");    //1006
        System.out.print("\"C:\\Download\\hello.cpp\"");    //1007
        System.out.print("\u250c\u252c\u2510\n\u251c\u253c\u2524\n\u2514\u2534\u2518");    //1008

        System.out.println(n);    //1010
        System.out.println(ch);    //1011

    }
}