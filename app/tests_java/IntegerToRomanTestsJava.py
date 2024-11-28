import subprocess
import os

class IntegerToRomanTestsJava():

    def __init__(self) -> None:
        self._tests = [
            [1, "I"],
            [4, "IV"],
            [9, "IX"],
            [58, "LVIII"],
            [1994, "MCMXCIV"],
            [2023, "MMXXIII"],
            [4000, "MMMM"],
        ]
    
    def tests(self, code):
        java_file = "app/problem_solver_java/IntegerToRoman.java"
        
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        int num = Integer.parseInt(args[0]);  // Convertir el argumento a un entero
        System.out.println(IntegerToRoman.integerToRoman(num));  // Llamada a la función estática integerToRoman
    }
}
        """
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/IntegerToRoman.java", java_runner_file], 
            capture_output=True, text=True
        )

        if compilacion.returncode != 0:
            return ("Error de compilación:", compilacion.stderr)
        else:
            resultados = []

            for entrada, esperado in self._tests:
                ejecucion = subprocess.run(
                    ["java", "-cp", "app/problem_solver_java", "RunMiClase", str(entrada)],
                    capture_output=True, text=True
                )

                if ejecucion.returncode == 0:
                    resultado = ejecucion.stdout.strip()
                    resultados.append(resultado == esperado)
                else:
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/IntegerToRoman.class")
            return resultados
