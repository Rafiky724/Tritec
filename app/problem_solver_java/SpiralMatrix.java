import java.util.ArrayList;
import java.util.List;

public class SpiralMatrix {
    public static List<Integer> spiralMatrix(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        
        // Verificar si la matriz está vacía
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return result;
        }

        int top = 0, bottom = matrix.length - 1;
        int left = 0, right = matrix[0].length - 1;

        while (top <= bottom && left <= right) {
            // Recorrer de izquierda a derecha en la fila superior
            for (int i = left; i <= right; i++) {
                result.add(matrix[top][i]);
            }
            top++;

            // Recorrer de arriba a abajo en la columna derecha
            for (int i = top; i <= bottom; i++) {
                result.add(matrix[i][right]);
            }
            right--;

            // Recorrer de derecha a izquierda en la fila inferior (si aún es válida)
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    result.add(matrix[bottom][i]);
                }
                bottom--;
            }

            // Recorrer de abajo a arriba en la columna izquierda (si aún es válida)
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    result.add(matrix[i][left]);
                }
                left++;
            }
        }

        return result;
    }
}