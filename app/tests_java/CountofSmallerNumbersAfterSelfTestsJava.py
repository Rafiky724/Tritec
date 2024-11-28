import subprocess
import os

class CountSmallerTestsJava():

    def __init__(self) -> None:
        self._tests = [
            ([1, 2, 3, 4, 5], [0, 0, 0, 0, 0]),  
            ([5, 2, 6, 1], [2, 1, 1, 0]),  
            ([-1, -1], [0, 0]),  
            ([5, 8, 7, 9, 2, 1], [2, 3, 2, 2, 1, 0])
        ]
    
    def tests(self, code):
        java_file = "app/problem_solver_java/CountSmaller.java"
        
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        // Parseamos el array de entrada
        String[] strArr = args[0].split(",");
        int[] nums = new int[strArr.length];
        for (int i = 0; i < strArr.length; i++) {
            nums[i] = Integer.parseInt(strArr[i].trim());
        }
        
        // Llamamos a la función countSmaller y mostramos el resultado
        int[] result = CountSmaller.countSmaller(nums);
        for (int i : result) {
            System.out.print(i + " ");
        }
    }
}
        """
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/CountSmaller.java", java_runner_file], 
            capture_output=True, text=True
        )

        if compilacion.returncode != 0:
            return ("Error de compilación:", compilacion.stderr)
        else:

            resultados = []

            for entrada, esperado in self._tests:

                entrada_str = ",".join(map(str, entrada))
                
                ejecucion = subprocess.run(
                    ["java", "-cp", "app/problem_solver_java", "RunMiClase", entrada_str],
                    capture_output=True, text=True
                )

                if ejecucion.returncode == 0:
                    resultado = list(map(int, ejecucion.stdout.strip().split()))
                    resultados.append(esperado == resultado)
                else:
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/CountSmaller.class")
            return resultados
