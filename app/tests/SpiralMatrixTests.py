import importlib
import sys

class SpiralMatrixTest():
    
    def __init__(self) -> None:
        self._test = [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
            ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
            ([[1]], [1]),
            ([[1, 2], [3, 4]], [1, 2, 4, 3]),
            ([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 6, 5, 4]),
            ([[1, 2, 3, 4], [5, 6, 7, 8]], [1, 2, 3, 4, 8, 7, 6, 5]),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]),
            ([[]], []), 
        ]
        
    def tests(self, name):

        try:
            # Eliminar cualquier referencia anterior al módulo en sys.modules
            if 'app.problem_solver.spiralmatrix' in sys.modules:
                del sys.modules['app.problem_solver.spiralmatrix']
        except Exception as e:
            pass

        self.reload_module(name)
        
        resultados = []
        for entrada, esperado in self._test:
            try:
                from app.problem_solver.spiralmatrix import spiralmatrix
                resultado = spiralmatrix(entrada)
                print(f"Resultado: {resultado}, esperado: {esperado}")
            except Exception as e:
                return f"Error: {e}"
            resultados.append(resultado == esperado)
        return resultados
    
    def reload_module(self, name):
        module_name = f"app.problem_solver.spiralmatrix"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)
        
        