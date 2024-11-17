import subprocess
import os

class IntegerToRomanTestsJava():

    def __init__(self) -> None:
        # Tests: (entrada, resultado esperado)
        self._tests = [
            [1, "I"],
            [4, "IV"],
            [9, "IX"],
            [58, "LVIII"],
            [1994, "MCMXCIV"],
            [2023, "MMXXIII"],
            [4000, "MMMM"],  # Este es un número válido que sobrepasa el límite tradicional de 3999
        ]
    
    def tests(self, code):
        # Ruta donde guardaremos el archivo de la clase IntegerToRoman
        java_file = "app/problem_solver_java/IntegerToRoman.java"
        
        # Guardamos el código de IntegerToRoman en el archivo Java
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        # Generamos el código del runner para ejecutar la función integerToRoman
        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        int num = Integer.parseInt(args[0]);  // Convertir el argumento a un entero
        System.out.println(IntegerToRoman.integerToRoman(num));  // Llamada a la función estática integerToRoman
    }
}
        """
        # Guardamos el código del runner en su archivo
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        # Compilamos ambos archivos juntos: IntegerToRoman.java y RunMiClase.java
        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/IntegerToRoman.java", java_runner_file], 
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
                # Ejecutamos el programa con la entrada correspondiente
                ejecucion = subprocess.run(
                    ["java", "-cp", "app/problem_solver_java", "RunMiClase", str(entrada)],
                    capture_output=True, text=True
                )

                # Si el código Java se ejecutó correctamente, capturamos la salida
                if ejecucion.returncode == 0:
                    resultado = ejecucion.stdout.strip()
                    print(f"IntegerToRoman de {entrada}: ", resultado)
                    resultados.append(resultado == esperado)
                else:
                    print("Error en la ejecución:", ejecucion.stderr)
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/IntegerToRoman.class")
            return resultados
