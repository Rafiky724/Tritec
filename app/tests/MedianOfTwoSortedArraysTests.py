import importlib
import sys

class MedianOfTwoSortedArraysTests():
    
    def __init__(self) -> None:
        self._tests = [
            ([[1, 3], [2]], 2),
            ([[1, 2], [3, 4]], 2.5),
            ([[1, 2], [4, 5, 3, 6]], 3.5),
            ([[1, 3, 4], [2, 5]], 3),
            ([[1, 3, 2, 4, 7], [6, 5, 8, 9, 10]], 5.5), 
        ]
    
    def tests(self, name):
        
        try:
            if 'app.problem_solver.medianoftwosortedarrays' in sys.modules:
                del sys.modules['app.problem_solver.medianoftwosortedarrays']
        except Exception as e:
            pass
        
        self.reload_module(name)
        
        resultados = []
        for entrada, esperado in self._tests:
            try:
                from app.problem_solver.medianoftwosortedarrays import median_of_two_sorted_arrays
                resultado =  median_of_two_sorted_arrays(entrada[0], entrada[1])
                print(f"Resultado: {resultado}, esperado: {esperado}")
            except Exception as e:
                return f"Error: {e}"
            resultados.append(resultado == esperado)
        return resultados
    
    def reload_module(self, name):
        module_name = f"app.problem_solver.medianoftwosortedarrays"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)
    
            
        