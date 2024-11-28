import subprocess
import os

class MedianOfTwoSortedArraysTestsJava():

    def __init__(self) -> None:
        self._tests = [
            ([[1, 3], [2]], 2),
            ([[1, 2], [3, 4]], 2.5),
            ([[1, 2], [4, 5, 3, 6]], 3.5),
            ([[1, 3, 4], [2, 5]], 3),
            ([[1, 3, 2, 4, 7], [6, 5, 8, 9, 10]], 5.5), 
        ]
    
    def tests(self, code):
        java_file = "app/problem_solver_java/MedianOfTwoSortedArrays.java"
        
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        // Parseamos los arreglos de entrada
        String[] array1Str = args[0].split(",");
        String[] array2Str = args[1].split(",");
        
        int[] array1 = new int[array1Str.length];
        for (int i = 0; i < array1Str.length; i++) {
            array1[i] = Integer.parseInt(array1Str[i]);
        }
        
        int[] array2 = new int[array2Str.length];
        for (int i = 0; i < array2Str.length; i++) {
            array2[i] = Integer.parseInt(array2Str[i]);
        }
        
        // Llamamos a la función medianOfTwoSortedArrays y mostramos el resultado
        System.out.println(MedianOfTwoSortedArrays.medianOfTwoSortedArrays(array1, array2));
    }
}
        """
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/MedianOfTwoSortedArrays.java", java_runner_file], 
            capture_output=True, text=True
        )

        if compilacion.returncode != 0:
            return ("Error de compilación:", compilacion.stderr)
        else:

            resultados = []

            for arrays, esperado in self._tests:
                array1_str = ",".join(map(str, arrays[0]))
                array2_str = ",".join(map(str, arrays[1]))

                ejecucion = subprocess.run(
                    ["java", "-cp", "app/problem_solver_java", "RunMiClase", array1_str, array2_str],
                    capture_output=True, text=True
                )

                if ejecucion.returncode == 0:
                    resultado = float(ejecucion.stdout.strip())
                    resultados.append(esperado == resultado)
                else:
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/MedianOfTwoSortedArrays.class")
            return resultados
