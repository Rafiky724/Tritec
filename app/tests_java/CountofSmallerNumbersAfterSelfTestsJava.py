import subprocess
import os

class CountSmallerTestsJava():

    def __init__(self) -> None:
        # Tests: (entrada, resultado esperado)
        self._tests = [
            ([1, 2, 3, 4, 5], [0, 0, 0, 0, 0]),  
            ([5, 2, 6, 1], [2, 1, 1, 0]),  
            ([-1, -1], [0, 0]),  
            ([5, 8, 7, 9, 2, 1], [2, 3, 2, 2, 1, 0])
        ]
    
    def tests(self, code):
        java_file = "app/problem_solver_java/CountSmaller.java"
        
        # Guardamos el código de CountSmaller en el archivo Java
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(code)

        # Generamos el código del runner para ejecutar la función countSmaller
        java_runner_file = "app/problem_solver_java/RunMiClase.java"
        codigo_runner = """
public class RunMiClase {
    public static void main(String[] args) {
        // Parseamos el array de entrada
        String[] strArr = args[0].split(",");
        int[] nums = new int[strArr.length];
        for (int i = 0; i < strArr.length; i++) {
            nums[i] = Integer.parseInt(strArr[i].trim());
        }
        
        // Llamamos a la función countSmaller y mostramos el resultado
        int[] result = CountSmaller.countSmaller(nums);
        for (int i : result) {
            System.out.print(i + " ");
        }
    }
}
        """
        # Guardamos el código del runner en su archivo
        with open(java_runner_file, "w", encoding="utf-8") as f:
            f.write(codigo_runner)

        # Compilamos ambos archivos juntos: CountSmaller.java y RunMiClase.java
        compilacion = subprocess.run(
            ["javac", "-encoding", "UTF-8", "app/problem_solver_java/CountSmaller.java", java_runner_file], 
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

                # Convertimos la entrada a formato string, ya que Java recibirá el array como argumento de cadena
                entrada_str = ",".join(map(str, entrada))
                
                # Ejecutamos el programa con la cadena como entrada
                ejecucion = subprocess.run(
                    ["java", "-cp", "app/problem_solver_java", "RunMiClase", entrada_str],
                    capture_output=True, text=True
                )

                # Si el código Java se ejecutó correctamente, capturamos la salida
                if ejecucion.returncode == 0:
                    # Comparamos el resultado con el esperado (convertimos la salida a lista de enteros)
                    resultado = list(map(int, ejecucion.stdout.strip().split()))
                    print(f"Count of smaller numbers after {entrada}: ", resultado)
                    resultados.append(esperado == resultado)
                else:
                    print("Error en la ejecución:", ejecucion.stderr)
                    resultados.append(False)
                
            os.remove(java_runner_file)
            os.remove("app/problem_solver_java/RunMiClase.class")
            os.remove("app/problem_solver_java/CountSmaller.class")
            return resultados
