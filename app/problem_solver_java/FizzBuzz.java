public class FizzBuzz {
    
    public static String fizzBuzz(int numero) {
        if (numero % 3 == 0 && numero % 5 == 0) {
            return "FizzBuzz"; // Si es divisible por 3 y 5, retorna "FizzBuzz"
        } else if (numero % 3 == 0) {
            return "Fizz"; // Si es divisible solo por 3, retorna "Fizz"
        } else if (numero % 5 == 0) {
            return "Buzz"; // Si es divisible solo por 5, retorna "Buzz"
        } else {
            return Integer.toString(numero); // Si no es divisible ni por 3 ni por 5, retorna el número
        }
    }
}
        