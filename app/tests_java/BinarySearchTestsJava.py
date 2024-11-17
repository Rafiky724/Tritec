import subprocess
import os

class BinarySearchTestsJava():

    def __init__(self) -> None:
        # Estos son los test que se van a ejecutar
        self._tests = [
            ([1, 2, 3, 4, 5], 3, 2),  # El número 3 está en el índice 2
            ([10, 20, 30, 40, 50], 10, 0),  # El número 10 está en el índice 0
            ([10, 20, 30, 40, 50], 50, 4),  # El número 50 está en el índice 4
            ([5, 7, 11, 17, 19], 13, -1),  # El número 13 no está en el array, debería devolver -1
            ([], 1, -1)  # El array está vacío, por lo que el resultado será -1
        ]
    
    def tests(self, code):
        # Ruta donde guardaremos el archivo de la clase BinarySearch
        java_file = "app/problem_solver_java/BinarySearch.java"
        
        # Guardamos el código de BinarySearch en el archivo Java
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        # Generamos el código del runner para ejecutar la función binarySearch
        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        int[] arr = new int[args.length - 1];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(args[i]);
        }
        int target = Integer.parseInt(args[args.length - 1]);
        System.out.println(BinarySearch.binarySearch(arr, target));  // Llamada a la función estática binarySearch de BinarySearch
    }
}
        """
        # Guardamos el código del runner en su archivo
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        # Compilamos ambos archivos juntos: BinarySearch.java y RunMiClase.java
        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/BinarySearch.java", java_runner_file], 
            capture_output=True, text=True
        )

        # Si hay errores de compilación, los mostramos
        if compilacion.returncode != 0:
            print("Detalles del error:", compilacion.stderr)
            return ("Error de compilación:", compilacion.stderr)
        else:
            print("Compilación exitosa")

            resultados = []

            for entrada, objetivo, esperado in self._tests:
                # Convertimos el array a string y pasamos el target al final
                args = [str(num) for num in entrada] + [str(objetivo)]
                
                ejecucion = subprocess.run(
                    ["java", "-cp", "app/problem_solver_java", "RunMiClase"] + args,
                    capture_output=True, text=True
                )

                # Si el código Java se ejecutó correctamente, capturamos la salida
                if ejecucion.returncode == 0:
                    print(f"BinarySearch de {entrada} con objetivo {objetivo}: ", ejecucion.stdout.strip())
                    resultados.append(int(ejecucion.stdout.strip()) == esperado)
                else:
                    print("Error en la ejecución:", ejecucion.stderr)
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/BinarySearch.class")
            return resultados
