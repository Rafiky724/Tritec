import subprocess
import os

class PalindromeTestsJava():

    def __init__(self) -> None:
        # Tests: (entrada, resultado esperado)
        self._tests = [
            ("racecar", True),
            ("level", True),
            ("hello", False),
            ("", True),
            ("A man a plan a canal Panama", True)  # Este es un palíndromo ignorando espacios y mayúsculas/minúsculas
        ]
    
    def tests(self, code):
        # Ruta donde guardaremos el archivo de la clase Palindrome
        java_file = "app/problem_solver_java/Palindrome.java"
        
        # Guardamos el código de Palindrome en el archivo Java
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        # Generamos el código del runner para ejecutar la función isPalindrome
        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        String word = String.join(" ", args);  // Unir los argumentos para formar la palabra
        System.out.println(Palindrome.isPalindrome(word));  // Llamada a la función estática isPalindrome de Palindrome
    }
}
        """
        # Guardamos el código del runner en su archivo
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        # Compilamos ambos archivos juntos: Palindrome.java y RunMiClase.java
        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/Palindrome.java", java_runner_file], 
            capture_output=True, text=True
        )

        # Si hay errores de compilación, los mostramos
        if compilacion.returncode != 0:
            print("Detalles del error:", compilacion.stderr)
            return ("Error de compilación:", compilacion.stderr)
        else:
            print("Compilación exitosa")

            resultados = []

            for entrada, esperado in self._tests:
                # Los argumentos se pasan como una lista de strings (palabra con espacios)
                args = entrada.split()  # Convertir la entrada en una lista de palabras
                
                ejecucion = subprocess.run(
                    ["java", "-cp", "app/problem_solver_java", "RunMiClase"] + args,
                    capture_output=True, text=True
                )

                # Si el código Java se ejecutó correctamente, capturamos la salida
                if ejecucion.returncode == 0:
                    resultado = ejecucion.stdout.strip() == 'true'
                    print(f"Palindromo de '{entrada}': ", resultado)
                    resultados.append(resultado == esperado)
                else:
                    print("Error en la ejecución:", ejecucion.stderr)
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/Palindrome.class")
            return resultados
