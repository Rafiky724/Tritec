import importlib
import sys

class PalindromeTests():

    def __init__(self) -> None:
        # Tests: (entrada, resultado esperado)
        self._tests = [
            ("racecar", True),
            ("level", True),
            ("hello", False),
            ("", True),
            ("A man a plan a canal Panama", True) 
        ]

    def tests(self, name):

        try:
            # Eliminar cualquier referencia anterior al módulo en sys.modules
            if 'app.problem_solver.palindrome' in sys.modules:
                del sys.modules['app.problem_solver.palindrome']
        except Exception as e:
            pass

        self.reload_module(name)

        resultados = []

        for palabra, esperado in self._tests:

            try:
                from app.problem_solver.palindrome import is_palindrome
                resultado = is_palindrome(palabra)
                print(f"Resultado: {resultado}, esperado: {esperado}")
            except Exception as e:
                return f"Error: {e}"
            resultados.append(resultado == esperado)

        return resultados

    def reload_module(self, name2):
        module_name = f"app.problem_solver.palindrome"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)
