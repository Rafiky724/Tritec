import subprocess
import os

class MedianOfTwoSortedArraysTestsJava():

    def __init__(self) -> None:
        # Tests: (entrada, resultado esperado)
        self._tests = [
            ([[1, 3], [2]], 2),
            ([[1, 2], [3, 4]], 2.5),
            ([[1, 2], [4, 5, 3, 6]], 3.5),
            ([[1, 3, 4], [2, 5]], 3),
            ([[1, 3, 2, 4, 7], [6, 5, 8, 9, 10]], 5.5), 
        ]
    
    def tests(self, code):
        java_file = "app/problem_solver_java/MedianOfTwoSortedArrays.java"
        
        # Guardamos el código de MedianOfTwoSortedArrays en el archivo Java
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        # Generamos el código del runner para ejecutar la función medianOfTwoSortedArrays
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
        # Guardamos el código del runner en su archivo
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        # Compilamos ambos archivos juntos: MedianOfTwoSortedArrays.java y RunMiClase.java
        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/MedianOfTwoSortedArrays.java", java_runner_file], 
            capture_output=True, text=True
        )

        # Si hay errores de compilación, los mostramos
        if compilacion.returncode != 0:
            print("Detalles del error:", compilacion.stderr)
            return ("Error de compilación:", compilacion.stderr)
        else:
            print("Compilación exitosa")

            resultados = []

            for arrays, esperado in self._tests:
                # Convertimos los arrays en una cadena para pasarlos como argumentos
                array1_str = ",".join(map(str, arrays[0]))
                array2_str = ",".join(map(str, arrays[1]))

                # Ejecutamos el programa con los arrays como entrada
                ejecucion = subprocess.run(
                    ["java", "-cp", "app/problem_solver_java", "RunMiClase", array1_str, array2_str],
                    capture_output=True, text=True
                )

                # Si el código Java se ejecutó correctamente, capturamos la salida
                if ejecucion.returncode == 0:
                    resultado = float(ejecucion.stdout.strip())  # La mediana puede ser un número decimal
                    print(f"Mediana de {arrays[0]} y {arrays[1]}: ", resultado)
                    resultados.append(esperado == resultado)
                else:
                    print("Error en la ejecución:", ejecucion.stderr)
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/MedianOfTwoSortedArrays.class")
            return resultados
