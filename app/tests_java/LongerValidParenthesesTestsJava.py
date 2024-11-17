import subprocess
import os

class LongerValidParenthesesTestsJava():

    def __init__(self) -> None:
        # Tests: (entrada, resultado esperado)
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
        
        # Guardamos el código de LongerValidParentheses en el archivo Java
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        # Generamos el código del runner para ejecutar la función longerValidParentheses
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
        # Guardamos el código del runner en su archivo
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        # Compilamos ambos archivos juntos: LongerValidParentheses.java y RunMiClase.java
        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/LongerValidParentheses.java", java_runner_file], 
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

                # Ejecutamos el programa con el string como entrada
                ejecucion = subprocess.run(
                    ["java", "-cp", "app/problem_solver_java", "RunMiClase", entrada],
                    capture_output=True, text=True
                )

                # Si el código Java se ejecutó correctamente, capturamos la salida
                if ejecucion.returncode == 0:
                    resultado = int(ejecucion.stdout.strip())
                    print(f"Longest valid parentheses in {entrada}: ", resultado)
                    resultados.append(esperado == resultado)
                else:
                    print("Error en la ejecución:", ejecucion.stderr)
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/LongerValidParentheses.class")
            return resultados
