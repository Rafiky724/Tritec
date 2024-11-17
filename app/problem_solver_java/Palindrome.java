public class Palindrome {
    public static boolean isPalindrome(String word) {
        // Eliminar espacios y convertir a minúsculas
        word = word.replace(" ", "").toLowerCase();
        
        int length = word.length();
        for (int i = 0; i < length / 2; i++) {
            if (word.charAt(i) != word.charAt(length - i - 1)) {
                return false;
            }
        }
        return true;
    }
}
        