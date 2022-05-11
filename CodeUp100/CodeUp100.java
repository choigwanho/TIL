import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        char ch = sc.next().charAt(0);
        float x = sc.nextFloat();
        int a = sc.nextInt();
        int b = sc.nextInt();
        char y = sc.next().charAt(0);
        char z = sc.next().charAt(0);
        float w = sc.nextFloat();
        int c = sc.nextInt();
        String m = sc.next();
        String p = sc.next();
        String[] t = p.split("\\.");
        int t0 = Integer.parseInt(t[0]);
        int t1 = Integer.parseInt(t[1]);
        int t2 = Integer.parseInt(t[2]);
        String i = sc.next();
        String[] u = i.split("-");
      
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
        System.out.format("%f", x);    //1012 System.out.format 메소드도 printf와 똑같은 기능 제공
        System.out.print(a+" "+b);    //1013
        System.out.print(z+" "+y);    //1014
        System.out.printf("%.2f",w);    //1015 print는 괄호안 내용을 단순히 출력, printf는 C언어의 printf와 동일. %f %s 등을 쓰기위해 사용 
        System.out.print(c+" "+c+" "+c);    //1017
        System.out.print(m);    //1018
        System.out.printf("%04d.%02d.%02d", t0,t1,t2);    //1019 정규식 \\. (.은 임의의 한 문자를 의미, \은 escape \뒤에 오는 문자를 일반문자로 취급, \. 정규식에서 일반문자 마침표를 의미 )
        System.out.println(u[0]+u[1]);    //1020
    }
}