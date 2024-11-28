import subprocess
import os

class FizzBuzzTestsJava():

    def __init__(self) -> None:
        self._tests = [
            [3, "Fizz"], [5, "Buzz"], [15, "FizzBuzz"], [2, "2"], 
            [7, "7"], [0, "FizzBuzz"], [901352955, "FizzBuzz"], [-1, "-1"]
        ]
    
    def tests(self, code):
        java_file = "app/problem_solver_java/FizzBuzz.java"
        
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        int a = Integer.parseInt(args[0]);
        System.out.println(FizzBuzz.fizzBuzz(a));  // Llamada a la función estática fizzBuzz de FizzBuzz
    }
}
        """
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/FizzBuzz.java", java_runner_file], 
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
                    resultados.append(esperado == ejecucion.stdout.strip())
                else:

                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/FizzBuzz.class")
            return resultados