import java.util.Stack;

public class LongerValidParentheses {
    public static int longerValidParentheses(String s) {
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);  // Agregar un marcador inicial para manejar casos como "()"

        int maxLength = 0;

        for (int i = 0; i < s.length(); i++) {
            char charAt = s.charAt(i);

            if (charAt == '(') {
                // Coloca el índice del paréntesis de apertura en la pila
                stack.push(i);
            } else if (charAt == ')') {
                // Desapilar el índice del paréntesis de apertura correspondiente
                stack.pop();

                // Si la pila no está vacía, calcular la longitud del paréntesis válido
                if (!stack.isEmpty()) {
                    maxLength = Math.max(maxLength, i - stack.peek());
                } else {
                    // Si la pila está vacía, agregamos el índice actual como marcador base
                    stack.push(i);
                }
            }
        }

        return maxLength/2;
    }
}
        