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
        
        # Guardamos el código de FizzBuzz en el archivo Java
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        # Generamos el código del runner para ejecutar la función fizzBuzz
        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        int a = Integer.parseInt(args[0]);
        System.out.println(FizzBuzz.fizzBuzz(a));  // Llamada a la función estática fizzBuzz de FizzBuzz
    }
}
        """
        # Guardamos el código del runner en su archivo
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        # Compilamos ambos archivos juntos: FizzBuzz.java y RunMiClase.java
        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/FizzBuzz.java", java_runner_file], 
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

                ejecucion = subprocess.run(
                    ["java", "-cp", "app/problem_solver_java", "RunMiClase", str(entrada)],
                    capture_output=True, text=True
                )

                # Si el código Java se ejecutó correctamente, capturamos la salida
                if ejecucion.returncode == 0:
                    print(f"Fizzbuzz de {entrada}: ", ejecucion.stdout.strip())
                    resultados.append(esperado == ejecucion.stdout.strip())
                else:
                    print("Error en la ejecución:", ejecucion.stderr)

                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/FizzBuzz.class")
            return resultados