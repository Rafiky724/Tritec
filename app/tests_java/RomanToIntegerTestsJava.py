import subprocess
import os

class RomanToIntegerTestsJava():

    def __init__(self) -> None:
        # Tests: (entrada, resultado esperado)
        self._tests = [
            ["I", 1],
            ["IV", 4],
            ["IX", 9],
            ["LVIII", 58],
            ["MCMXCIV", 1994],
            ["MMXXIII", 2023],
        ]
    
    def tests(self, code):
        # Ruta donde guardaremos el archivo de la clase RomanToInteger
        java_file = "app/problem_solver_java/RomanToInteger.java"
        
        # Guardamos el código de RomanToInteger en el archivo Java
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        # Generamos el código del runner para ejecutar la función romanToInteger
        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        String num = args[0];  // El número romano como cadena de caracteres
        System.out.println(RomanToInteger.romanToInteger(num));  // Llamada a la función estática romanToInteger
    }
}
        """
        # Guardamos el código del runner en su archivo
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        # Compilamos ambos archivos juntos: RomanToInteger.java y RunMiClase.java
        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/RomanToInteger.java", java_runner_file], 
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
                # Ejecutamos el programa con el número romano correspondiente
                ejecucion = subprocess.run(
                    ["java", "-cp", "app/problem_solver_java", "RunMiClase", entrada],
                    capture_output=True, text=True
                )

                # Si el código Java se ejecutó correctamente, capturamos la salida
                if ejecucion.returncode == 0:
                    resultado = int(ejecucion.stdout.strip())
                    print(f"RomanToInteger de '{entrada}': ", resultado)
                    resultados.append(resultado == esperado)
                else:
                    print("Error en la ejecución:", ejecucion.stderr)
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/RomanToInteger.class")
            return resultados
