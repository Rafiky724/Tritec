import importlib
import sys

try:
    from app.tests.BinarySearchTests import BinarySearchTests
    from app.tests.PalindromeTests import PalindromeTests
    from app.tests.FizzBuzzTests import FizzBuzzTests
    from app.tests.IntegerToRomanTests import IntegerToRomanTests
    from app.tests.RomanToIntegerTests import RomanToIntegerTests
    from app.tests.MoneyToEnglishTests import MoneyToEnglishTests
    from app.tests.TowerOfHanoiTests import TowerOfHanoiTests
    from app.tests.SpiralMatrixTests import SpiralMatrixTest


except ImportError as e:
    print(f"Error: Unable to import. {str(e)}")

class CodesController():

    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name

    def write_code(self):
        file_name = f"app/problem_solver/{self.name.lower()}.py"

        try:
            with open(file_name, 'w') as file:
                file.write(self.code)
            print(f"El código ha sido escrito correctamente en {file_name}")
            return True
        except ImportError as e:
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
                
                if self.name == 'IntegerToRoman':
                    tests_integerToRoman = IntegerToRomanTests()
                    return tests_integerToRoman.tests(self.name)
                
                if self.name == 'RomanToInteger':
                    tests_romanToInteger = RomanToIntegerTests()
                    return tests_romanToInteger.tests(self.name)
                
                if self.name == 'MoneyToEnglish':
                    tests_moneyToEnglish = MoneyToEnglishTests()
                    print(tests_moneyToEnglish)
                    return tests_moneyToEnglish.tests(self.name)
                
                if self.name == "TowerOfHanoi":
                    tests_towerofhanoi =  TowerOfHanoiTests()  
                    return tests_towerofhanoi.tests(self.name) 

                 if self.name == "SpiralMatrix":
                    tests_SpiralMatrix =  SpiralMatrixTest()  
                    return tests_SpiralMatrix.tests(self.name)  
                


            except ImportError as e:
                print(f"Error al cargar el módulo {self.name}: {e}")

        return []

    def reload_module(self):
        module_name = f"app.problem_solver.{self.name.lower()}"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)
