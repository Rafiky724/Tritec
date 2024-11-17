import subprocess
import os

class MoneyToEnglishTestsJava():

    def __init__(self) -> None:
        # Tests: (entrada, resultado esperado)
        self._tests = [
            (0, "zero dollars"),
            (1, "one dollar"),
            (2.55, "two dollars and fifty five cents"),
            (10, "ten dollars"),
            (20.01, "twenty dollars and one cent"),
            (100, "one hundred dollars"),
            (105.74, "one hundred five dollars and seventy four cents"),
            (1000, "one thousand dollars"),
            (-5, "negative five dollars"),
            (-105, "negative one hundred five dollars"),
        ]
    
    def tests(self, code):
        # Ruta donde guardaremos el archivo de la clase MoneyToEnglish
        java_file = "app/problem_solver_java/MoneyToEnglish.java"
        
        # Guardamos el código de MoneyToEnglish en el archivo Java
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        # Generamos el código del runner para ejecutar la función moneyToEnglish
        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        double num = Double.parseDouble(args[0]);  // Convertir el argumento a un número decimal
        System.out.println(MoneyToEnglish.moneyToEnglish(num));  // Llamada a la función estática moneyToEnglish
    }
}
        """
        # Guardamos el código del runner en su archivo
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        # Compilamos ambos archivos juntos: MoneyToEnglish.java y RunMiClase.java
        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/MoneyToEnglish.java", java_runner_file], 
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
                    print(f"MoneyToEnglish de {entrada}: ", resultado)
                    resultados.append(resultado == esperado)
                else:
                    print("Error en la ejecución:", ejecucion.stderr)
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/MoneyToEnglish.class")
            return resultados
