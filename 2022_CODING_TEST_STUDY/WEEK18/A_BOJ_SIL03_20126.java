/* 
* 2022.05.17 (화) 
* BOJ_SIL03_20126
* 18주차 A - 교수님의 기말고사
*/

import java.io.*;
import java.util.*;

class Exam implements Comparable<Exam>{
    int x, y;
    
    public Exam(int x, int y){
        this.x = x;
        this.y = y;
    }

    @Override
    public int ComparaTo(Exam o){
        if(this.x ==o.x)
            return this.y - o.y;
        return this.x - o.x;
    }
}

public class Main{
    static FastReader scan = new FastReader();
    static StringBuiler sb = new StringBuilder();

    static int n,m,s;
    
    static void input(){
        int n = scan.nextInt();
        int m = scan.nextInt();
        int s = scan.nextInt();  
    }

    static void sol_func(int n){

        Exam[] arr = new Exam(n+2);
        arr[0] = new Exam(0,0);
        for(int i = 1; i <= n; i++){
            arr[i] = new Exam(nextInt(), nextInt());
        }
        arr[n+1] = new Exam(s,s);
        Arrays.sort(arr);

        for(int i=1;i<arr.length;i++){
            if(arr[i].x-(arr[i-1].x+arr[i-1].y)>=m){
                System.out.println(arr[i-1].x+arr[i-1].y);
                return;
            }
        }
        System.out.println(-1);
    }
    
    public static void main(String[] args){
        input();
        sol_func(n);
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
        double nextDouble() {
            return Double.parseDouble(next());
        }
        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}