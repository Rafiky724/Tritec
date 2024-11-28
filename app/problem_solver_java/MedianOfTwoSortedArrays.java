import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MedianOfTwoSortedArrays {
    public static double medianOfTwoSortedArrays(int[] array1, int[] array2) {
        // Crear una lista para combinar ambos arrays
        int[] combinedArray = new int[array1.length + array2.length];
        
        // Copiar los elementos de ambos arrays a la lista combinada
        System.arraycopy(array1, 0, combinedArray, 0, array1.length);
        System.arraycopy(array2, 0, combinedArray, array1.length, array2.length);
        
        // Ordenar el array combinado
        Arrays.sort(combinedArray);
        
        // Calcular el tamaño del array combinado
        int size = combinedArray.length;
        
        // Si el tamaño es impar, la mediana es el valor del medio
        if (size % 2 == 1) {
            return combinedArray[size / 2];
        } else {
            // Si el tamaño es par, la mediana es el promedio de los dos valores centrales
            return (combinedArray[size / 2 - 1] + combinedArray[size / 2]) / 2.0;
        }
    }
}