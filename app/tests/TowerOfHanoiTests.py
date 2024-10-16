import importlib
import sys

class TowerOfHanoiTests:

    def __init__(self) -> None:
        self._tests = [
            (1, 'A', 'C', 'B', [('A', 'C')]),
            (2, 'A', 'C', 'B', [('A', 'B'), ('A', 'C'), ('B', 'C')]),
            (3, 'A', 'C', 'B', [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]),
            (4, 'A', 'C', 'B', [
                ('A', 'B'), ('A', 'C'), ('B', 'C'), 
                ('A', 'B'), ('C', 'A'), ('C', 'B'), 
                ('A', 'B'), ('A', 'C'), ('B', 'C'), 
                ('B', 'A'), ('C', 'A'), ('B', 'C'), 
                ('A', 'B'), ('A', 'C'), ('B', 'C')
            ]),
        ]

    def tests(self, name):
        self.reload_module(name)

        resultados = []
        for entrada, esperado in self._tests:
            try:
                from app.problem_solver.Towerofhanoi import tower_of_hanoi 
                resultado = tower_of_hanoi(entrada)
                print(f"Resultado: {resultado}, esperado: {esperado}")
            except Exception as e:
                return f"Error: {e}"
            resultados.append(resultado == esperado)
        return resultados

    def reload_module(self, name):
        module_name = f"app.problem_solver.towerofhanoi"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)


