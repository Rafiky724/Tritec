import importlib
import sys

class CountofSmallerNumbersAfterSelfTests():

    def __init__(self) -> None:
       
       self._tests = [
            ([1, 2, 3, 4, 5], [0, 0, 0, 0, 0]),  
            ([5, 2, 6, 1], [2, 1, 1, 0]),  
            ([-1, -1], [0, 0]),  
            ([5, 8, 7, 9, 2, 1], [2, 3, 2, 2, 1, 0]),  
            ([], [])  
        ]

    def tests(self, name):

        try:
            if 'app.problem_solver.countofsmallernumbersafterself' in sys.modules:
                del sys.modules['app.problem_solver.countofsmallernumbersafterself']
        except Exception as e:
            pass

        self.reload_module(name)

        resultados = []

        for lista, esperado in self._tests:

            try:
                from app.problem_solver.countofsmallernumbersafterself import count_Smaller
                resultado = count_Smaller(lista)
            except Exception as e:
                return f"Error: {e}"
            resultados.append(resultado == esperado)

        return resultados

    def reload_module(self, name2):
        module_name = f"app.problem_solver.countofsmallernumbersafterself"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)
