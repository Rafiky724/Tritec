import java.util.HashMap;
import java.util.Map;

public class RomanToInteger {
    public static int romanToInteger(String num) {
        // Crear un mapa de los valores de los números romanos
        Map<Character, Integer> romanNumerals = new HashMap<>();
        romanNumerals.put('I', 1);
        romanNumerals.put('V', 5);
        romanNumerals.put('X', 10);
        romanNumerals.put('L', 50);
        romanNumerals.put('C', 100);
        romanNumerals.put('D', 500);
        romanNumerals.put('M', 1000);

        int total = 0;
        int prevValue = 0;

        // Recorrer el número romano de derecha a izquierda
        for (int i = num.length() - 1; i >= 0; i--) {
            char currentChar = num.charAt(i);
            int value = romanNumerals.get(currentChar);

            // Si el valor actual es menor que el valor anterior, restamos, sino sumamos
            if (value < prevValue) {
                total -= value;
            } else {
                total += value;
            }

            prevValue = value;  // Actualizamos el valor anterior
        }

        return total;
    }
}