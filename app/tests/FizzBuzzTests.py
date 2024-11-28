import importlib
import sys

class FizzBuzzTests():

    def __init__(self) -> None:
        self._tests = [[3, "Fizz"], [5, "Buzz"], [15, "FizzBuzz"], [2, "2"], [7, "7"],\
                       [0, "FizzBuzz"], [901352955, "FizzBuzz"], [-1, "-1"]]
        
    def tests(self, name):

        try:
            if 'app.problem_solver.fizzbuzz' in sys.modules:
                del sys.modules['app.problem_solver.fizzbuzz']
        except Exception as e:
            pass

        self.reload_module(name)

        resultados = []

        for entrada, esperado in self._tests:

            try:
                from app.problem_solver.fizzbuzz import fizzbuzz
                resultado = fizzbuzz(entrada)
            except Exception as e:
                return f"Error: {e}"
            resultados.append(resultado == esperado)


        return resultados

    def reload_module(self, name2):
        module_name = f"app.problem_solver.fizzbuzz"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)