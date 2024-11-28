import importlib
import sys

class RomanToIntegerTests:

    def __init__(self) -> None:
        self._tests = [
            ["I", 1],
            ["IV", 4],
            ["IX", 9],
            ["LVIII", 58],
            ["MCMXCIV", 1994],
            ["MMXXIII", 2023],
        ]

    def tests(self, name):

        try:
            if 'app.problem_solver.romantointeger' in sys.modules:
                del sys.modules['app.problem_solver.romantointeger']
        except Exception as e:
            pass

        self.reload_module(name)

        resultados = []
        for entrada, esperado in self._tests:
            try:
                from app.problem_solver.romantointeger import roman_to_integer
                resultado = roman_to_integer(entrada)
            except Exception as e:
                return f"Error: {e}"
            resultados.append(resultado == esperado)

        return resultados

    def reload_module(self, name):
        module_name = f"app.problem_solver.romantointeger"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)
