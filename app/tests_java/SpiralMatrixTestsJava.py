import subprocess
import os

class SpiralMatrixTestsJava():

    def __init__(self) -> None:
        # Tests: (entrada, resultado esperado)
        self._test = [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
            ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
            ([[1]], [1]),
            ([[1, 2], [3, 4]], [1, 2, 4, 3]),
            ([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 6, 5, 4]),
            ([[1, 2, 3, 4], [5, 6, 7, 8]], [1, 2, 3, 4, 8, 7, 6, 5]),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]),
        ]
    
    def tests(self, code):
        java_file = "app/problem_solver_java/SpiralMatrix.java"
        
        # Guardamos el código de SpiralMatrix en el archivo Java
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        # Generamos el código del runner para ejecutar la función spiralMatrix
        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        // Crear la matriz de entrada
        String[] input = args[0].split(";");
        int rows = input.length;
        int cols = input[0].split(",").length;
        int[][] matrix = new int[rows][cols];

        // Convertir la entrada a una matriz de enteros
        for (int i = 0; i < rows; i++) {
            String[] row = input[i].split(",");
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = Integer.parseInt(row[j]);
            }
        }

        // Llamada a la función spiralMatrix y mostrar el resultado
        System.out.println(SpiralMatrix.spiralMatrix(matrix));
    }
}
        """
        # Guardamos el código del runner en su archivo
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        # Compilamos ambos archivos juntos: SpiralMatrix.java y RunMiClase.java
        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/SpiralMatrix.java", java_runner_file], 
            capture_output=True, text=True
        )

        # Si hay errores de compilación, los mostramos
        if compilacion.returncode != 0:
            print("Detalles del error:", compilacion.stderr)
            return ("Error de compilación:", compilacion.stderr)
        else:
            print("Compilación exitosa")

            resultados = []

            for matriz, esperado in self._test:
                # Convertimos la matriz en una cadena para pasarla como argumento
                matriz_str = ";".join([",".join(map(str, fila)) for fila in matriz])

                # Ejecutamos el programa con la matriz como entrada
                ejecucion = subprocess.run(
                    ["java", "-cp", "app/problem_solver_java", "RunMiClase", matriz_str],
                    capture_output=True, text=True
                )

                # Si el código Java se ejecutó correctamente, capturamos la salida
                if ejecucion.returncode == 0:
                    # Limpiar la salida antes de convertir a enteros
                    cleaned_output = ejecucion.stdout.strip().strip('[]')  # Eliminar corchetes
                    resultado = list(map(int, cleaned_output.split(", ")))  # Convertir a enteros
                    print(f"SpiralMatrix de {matriz}: ", resultado)
                    resultados.append(resultado == esperado)
                else:
                    print("Error en la ejecución:", ejecucion.stderr)
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/SpiralMatrix.class")
            return resultados
