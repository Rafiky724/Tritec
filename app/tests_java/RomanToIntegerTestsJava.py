import subprocess
import os

class RomanToIntegerTestsJava():

    def __init__(self) -> None:
        self._tests = [
            ["I", 1],
            ["IV", 4],
            ["IX", 9],
            ["LVIII", 58],
            ["MCMXCIV", 1994],
            ["MMXXIII", 2023],
        ]
    
    def tests(self, code):
        java_file = "app/problem_solver_java/RomanToInteger.java"
        
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        String num = args[0];  // El número romano como cadena de caracteres
        System.out.println(RomanToInteger.romanToInteger(num));  // Llamada a la función estática romanToInteger
    }
}
        """
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/RomanToInteger.java", java_runner_file], 
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
                    resultados.append(resultado == esperado)
                else:
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/RomanToInteger.class")
            return resultados
