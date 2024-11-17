public class MoneyToEnglish {
    
    public static String moneyToEnglish(double num) {
        if (num < 0) {
            return "negative " + moneyToEnglish(-num);
        }

        // Arrays con las palabras correspondientes
        String[] units = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        String[] teens = {"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
                          "sixteen", "seventeen", "eighteen", "nineteen"};
        String[] tens = {"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

        // Si el número es 0
        if (num == 0) {
            return "zero dollars";
        }

        // Separar la parte de los dólares y los centavos
        int dollars = (int) num;
        int cents = (int) Math.round((num - dollars) * 100);

        StringBuilder words = new StringBuilder();

        // Convertir dólares a palabras
        if (dollars >= 1000) {
            words.append(units[dollars / 1000]).append(" thousand ");
            dollars %= 1000;
        }

        if (dollars >= 100) {
            words.append(units[dollars / 100]).append(" hundred ");
            dollars %= 100;
        }

        if (dollars >= 20) {
            words.append(tens[dollars / 10]).append(" ");
            dollars %= 10;
        }

        if (dollars >= 10) {
            words.append(teens[dollars - 10]).append(" ");
            dollars = 0;
        }

        if (dollars > 0) {
            words.append(units[dollars]).append(" ");
        }

        // Agregar "dollar" o "dollars"
        String dollarWords = words.toString().trim() + (words.toString().trim().equals("one") ? " dollar" : " dollars");

        // Si hay centavos, convertirlos a palabras
        if (cents > 0) {
            words.setLength(0); // Limpiar el StringBuilder para los centavos

            if (cents >= 20) {
                words.append(tens[cents / 10]).append(" ");
                cents %= 10;
            }

            if (cents >= 10) {
                words.append(teens[cents - 10]).append(" ");
                cents = 0;
            }

            if (cents > 0) {
                words.append(units[cents]).append(" ");
            }

            // Agregar "cent" o "cents"
            String centWords = words.toString().trim() + (words.toString().trim().equals("one") ? " cent" : " cents");
            return dollarWords + " and " + centWords;
        }

        return "asdasd";
    }
}
        