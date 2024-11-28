import subprocess
import os

class LongerValidParenthesesTestsJava():

    def __init__(self) -> None:
        self._tests = [
            ["(()())", 3],
            [")()())", 2],
            ["(()", 1],
            ["(((()))))", 4],
            ["((()())", 3],
            ["()", 1],
            ["", 0],  
        ]
    
    def tests(self, code):
        java_file = "app/problem_solver_java/LongerValidParentheses.java"
        
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        // Parseamos el string de entrada
        String s = args[0];
        
        // Llamamos a la función longerValidParentheses y mostramos el resultado
        System.out.println(LongerValidParentheses.longerValidParentheses(s));
    }
}
        """
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/LongerValidParentheses.java", java_runner_file], 
            capture_output=True, text=True
        )

        if compilacion.returncode != 0:
            return ("Error de compilación:", compilacion.stderr)
        else:

            resultados = []

            for entrada, esperado in self._tests:

                ejecucion = subprocess.run(
                    ["java", "-cp", "app/problem_solver_java", "RunMiClase", entrada],
                    capture_output=True, text=True
                )

                if ejecucion.returncode == 0:
                    resultado = int(ejecucion.stdout.strip())
                    resultados.append(esperado == resultado)
                else:
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/LongerValidParentheses.class")
            return resultados
