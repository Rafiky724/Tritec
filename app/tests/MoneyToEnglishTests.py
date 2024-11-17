import importlib
import sys

class MoneyToEnglishTests:

    def __init__(self) -> None:
        self._tests = [
            (0, "zero dollars"),
            (1, "one dollar"),
            (2.55, "two dollars and fifty five cents"),
            (10, "ten dollars"),
            (20.01, "twenty dollars and one cent"),
            (100, "one hundred dollars"),
            (105.74, "one hundred five dollars and seventy four cents"),
            (1000, "one thousand dollars"),
            (-5, "negative five dollars"),
            (-105, "negative one hundred five dollars"),       
        ]

    def tests(self, name):

        try:
            # Eliminar cualquier referencia anterior al módulo en sys.modules
            if 'app.problem_solver.moneytoenglish' in sys.modules:
                del sys.modules['app.problem_solver.moneytoenglish']
        except Exception as e:
            pass

        self.reload_module(name)

        resultados = []
        for entrada, esperado in self._tests:
            try:
                from app.problem_solver.moneytoenglish import money_to_english
                resultado = money_to_english(entrada)
                assert resultado == esperado, f"Resultado: {resultado}, esperado: {esperado}"
            except AssertionError as e:
                print(e)
                resultados.append(False)
            except Exception as e:
                print(f"Error: {e}")
                resultados.append(False)
            else:
                print(f"Prueba exitosa: {entrada} -> {resultado}")
                resultados.append(True)

        return resultados

    def reload_module(self, name):
        module_name = f"app.problem_solver.moneytoenglish"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)
