import subprocess
import os

class MoneyToEnglishTestsJava():

    def __init__(self) -> None:
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
        java_file = "app/problem_solver_java/MoneyToEnglish.java"
        
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        double num = Double.parseDouble(args[0]);  // Convertir el argumento a un número decimal
        System.out.println(MoneyToEnglish.moneyToEnglish(num));  // Llamada a la función estática moneyToEnglish
    }
}
        """
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/MoneyToEnglish.java", java_runner_file], 
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
            os.remove("app/problem_solver_java/MoneyToEnglish.class")
            return resultados
