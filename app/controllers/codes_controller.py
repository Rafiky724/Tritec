import importlib
import os
import sys

from app.tests.BinarySearchTests import BinarySearchTests
from app.tests.PalindromeTests import PalindromeTests
from app.tests.FizzBuzzTests import FizzBuzzTests

class CodesController():

    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name

    def write_code(self):
        file_name = f"app/problem_solver/{self.name.lower()}.py"  # Usar '/' para compatibilidad entre sistemas
        #print(f"Writing to file: {file_name}")

        try:
            with open(file_name, 'w') as file:
                file.write(self.code)
            print(f"El código ha sido escrito correctamente en {file_name}")
            return True
        except Exception as e:
            print(f"Error al escribir el código en el archivo {file_name}: {e}")
            return False

    def set_up(self):
        if self.write_code():

            try:

                self.reload_module()
                if self.name == 'FizzBuzz':
                    tests_fizz = FizzBuzzTests()
                    return tests_fizz.tests(self.name)

                if self.name == 'BinarySearch':
                    tests_binary_search = BinarySearchTests()
                    return tests_binary_search.tests(self.name)

                if self.name == 'Palindrome':
                    tests_palindrome = PalindromeTests()
                    return tests_palindrome.tests(self.name)

            except Exception as e:
                print(f"Error al cargar el módulo {self.name}: {e}")

        return []
    
    def reload_module(self):
        module_name = f"app.problem_solver.{self.name.lower()}"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)
    
    
        
