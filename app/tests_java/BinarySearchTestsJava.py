import subprocess
import os

class BinarySearchTestsJava():

    def __init__(self) -> None:
        self._tests = [
            ([1, 2, 3, 4, 5], 3, 2),
            ([10, 20, 30, 40, 50], 10, 0),
            ([10, 20, 30, 40, 50], 50, 4),
            ([5, 7, 11, 17, 19], 13, -1),
            ([], 1, -1)
        ]
    
    def tests(self, code):
        java_file = "app/problem_solver_java/BinarySearch.java"
        
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

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
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/BinarySearch.java", java_runner_file], 
            capture_output=True, text=True
        )

        if compilacion.returncode != 0:
            return ("Error de compilación:", compilacion.stderr)
        else:

            resultados = []

            for entrada, objetivo, esperado in self._tests:
                args = [str(num) for num in entrada] + [str(objetivo)]
                
                ejecucion = subprocess.run(
                    ["java", "-cp", "app/problem_solver_java", "RunMiClase"] + args,
                    capture_output=True, text=True
                )

                if ejecucion.returncode == 0:
                    resultados.append(int(ejecucion.stdout.strip()) == esperado)
                else:
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/BinarySearch.class")
            return resultados
