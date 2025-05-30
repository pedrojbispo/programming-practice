package Fibonacci_Solutions;
import java.util.ArrayList;

public class fibonacci_print {
    public static void main(String[] args){
        ArrayList<Integer> fib = new ArrayList<>();
        int fib_num = 0;
        for (int i=0;i<30;i++){
            if (i == 0){
                fib.add(0);
            }
            if (i == 1){
                fib.add(1);
            }
            if (i >= 2){
                fib_num = fib.get(i-1) + fib.get(i-2);
                fib.add(fib_num);
            }
        }
        System.out.println(fib);
    }
}
