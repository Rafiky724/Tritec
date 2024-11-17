import importlib
import sys

class LongerValidParenthesesTests():

    def __init__(self) -> None:
        self._tests = [
            ["(()())", 3],
            [")()())", 2],
            ["(()", 1],
            ["(((()))))", 4],
            ["((()())", 3],
            ["()", 1],
            ["", 0],  
        ]

    def tests(self, name):

        try:
            if 'app.problem_solver.longervalidparentheses' in sys.modules:
                del sys.modules['app.problem_solver.longervalidparentheses']
        except Exception as e:
            pass

        self.reload_module(name)

        resultados = []
        for entrada, esperado in self._tests:
            try:
                from app.problem_solver.longervalidparentheses import longer_valid_parentheses
                resultado = longer_valid_parentheses(entrada)
                print(f"Resultado: {resultado}, esperado: {esperado}")
            except Exception as e:
                return f"Error: {e}"
            resultados.append(resultado == esperado)

        return resultados

    def reload_module(self, name2):
        module_name = f"app.problem_solver.longervalidparentheses"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)
