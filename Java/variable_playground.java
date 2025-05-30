public class variable_playground {
    public static void main(String[] args){
        // In Java variables must be specified, unlike Python.
        int x = 0;
        String name = "Luis";
        System.out.println(x); // Java has an interesting print function, regular print only prints but println works like print but adds a new line at the end
        System.out.println(name);
        int y = 151342;
        int z = 3534;
        double t = 23.21;
        float l = 42.13f; // Float variables need "f" at the end. This tells Java that this variable is float and not a double.
        System.out.println(t * l);
        System.out.println(y + z);
        System.out.println(l % t);
        String person1 = "Lisa";
        char person2 = 'K'; // Char variables use the '' and not ""
        System.out.println(person2 + " Talked with " + person1);
    }
}
