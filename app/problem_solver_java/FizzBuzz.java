public class FizzBuzz {
    public static String fizzBuzz(int numero) {
        return (numero % 3 == 0 ? "Fizz" : "") + (numero % 5 == 0 ? "Buzz" : (numero % 3 != 0 ? Integer.toString(numero) : ""));
    }

} 