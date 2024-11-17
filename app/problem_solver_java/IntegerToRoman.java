public class IntegerToRoman {
    public static String integerToRoman(int num) {
        // Arreglo con los valores de los números romanos
        int[] val = {
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        };

        // Arreglo con los símbolos correspondientes a cada valor
        String[] syms = {
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        };

        // Cadena para almacenar el resultado
        StringBuilder romanNum = new StringBuilder();

        // Iterar sobre los valores romanos
        for (int i = 0; i < val.length; i++) {
            // Mientras el número sea mayor que el valor actual
            while (num >= val[i]) {
                romanNum.append(syms[i]);  // Añadir el símbolo correspondiente
                num -= val[i];             // Restar el valor de num
            }
        }

        return romanNum.toString();
    }
}
        