import subprocess
import os

class PalindromeTestsJava():

    def __init__(self) -> None:
        self._tests = [
            ("racecar", True),
            ("level", True),
            ("hello", False),
            ("", True),
            ("A man a plan a canal Panama", True)
        ]
    
    def tests(self, code):
        java_file = "app/problem_solver_java/Palindrome.java"
        
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        String word = String.join(" ", args);  // Unir los argumentos para formar la palabra
        System.out.println(Palindrome.isPalindrome(word));  // Llamada a la función estática isPalindrome de Palindrome
    }
}
        """
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/Palindrome.java", java_runner_file], 
            capture_output=True, text=True
        )

        if compilacion.returncode != 0:
            return ("Error de compilación:", compilacion.stderr)
        else:

            resultados = []

            for entrada, esperado in self._tests:
                args = entrada.split()
                
                ejecucion = subprocess.run(
                    ["java", "-cp", "app/problem_solver_java", "RunMiClase"] + args,
                    capture_output=True, text=True
                )

                if ejecucion.returncode == 0:
                    resultado = ejecucion.stdout.strip() == 'true'
                    resultados.append(resultado == esperado)
                else:
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/Palindrome.class")
            return resultados
