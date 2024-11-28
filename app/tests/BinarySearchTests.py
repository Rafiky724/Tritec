import importlib
import sys

class BinarySearchTests():

    def __init__(self) -> None:
       
        self._tests = [
            ([1, 2, 3, 4, 5], 3, 2),  
            ([10, 20, 30, 40, 50], 10, 0),  
            ([10, 20, 30, 40, 50], 50, 4), 
            ([5, 7, 11, 17, 19], 13, -1), 
            ([], 1, -1)  
        ]

    def tests(self, name):

        try:
            if 'app.problem_solver.binarysearch' in sys.modules:
                del sys.modules['app.problem_solver.binarysearch']
        except Exception as e:
            pass

        self.reload_module(name)

        resultados = []

        for lista, objetivo, esperado in self._tests:

            try:
                from app.problem_solver.binarysearch import binary_search
                resultado = binary_search(lista, objetivo)
            except Exception as e:
                return f"Error: {e}"
            resultados.append(resultado == esperado)

        return resultados

    def reload_module(self, name2):
        module_name = f"app.problem_solver.binarysearch"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)
