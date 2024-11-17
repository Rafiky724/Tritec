import importlib
import sys

class IntegerToRomanTests():

    def __init__(self) -> None:
        self._tests = [
            [1, "I"],
            [4, "IV"],
            [9, "IX"],
            [58, "LVIII"],
            [1994, "MCMXCIV"],
            [2023, "MMXXIII"],
            [4000, "MMMM"],  
        ]

    def tests(self, name):

        try:
            # Eliminar cualquier referencia anterior al módulo en sys.modules
            if 'app.problem_solver.integertoroman' in sys.modules:
                del sys.modules['app.problem_solver.integertoroman']
        except Exception as e:
            pass

        self.reload_module(name)

        resultados = []
        for entrada, esperado in self._tests:
            try:
                from app.problem_solver.integertoroman import integer_to_roman
                resultado = integer_to_roman(entrada)
                print(f"Resultado: {resultado}, esperado: {esperado}")
            except Exception as e:
                return f"Error: {e}"
            resultados.append(resultado == esperado)

        return resultados

    def reload_module(self, name2):
        module_name = f"app.problem_solver.integertoroman"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)
