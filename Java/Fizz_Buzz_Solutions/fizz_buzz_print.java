package Fizz_Buzz_Solutions;
import java.util.ArrayList;
public class fizz_buzz_print {
    public static void main(String[] args){
        ArrayList<Integer> fizz = new ArrayList<Integer>();
        ArrayList <Integer> buzz = new ArrayList<Integer>();
        ArrayList <Integer> fizzbuzz = new ArrayList<Integer>();
        ArrayList <Integer> outnumbers = new ArrayList<Integer>();

        for (int i=1; i<50; i++){
            if (i % 3 == 0 & i % 5 != 0){
                fizz.add(i);
                System.out.println("Fizz");
            }
            if (i % 5 == 0 & i % 3 != 0){
                buzz.add(i);
                System.out.println("Buzz");
            }
            if (i % 3 == 0 & i % 5 == 0){
                fizzbuzz.add(i);
                System.out.println("FizzBuzz");
            }
            if (i % 3 != 0 & i % 5 != 0){
                outnumbers.add(i);
                System.out.println(i);
            }
        }
    }
}
