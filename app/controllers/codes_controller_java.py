try:
    from app.tests_java.FizzBuzzTestsJava import FizzBuzzTestsJava
    from app.tests_java.BinarySearchTestsJava import BinarySearchTestsJava
    from app.tests_java.PalindromeTestsJava import PalindromeTestsJava
    from app.tests_java.IntegerToRomanTestsJava import IntegerToRomanTestsJava
    from app.tests_java.RomanToIntegerTestsJava import RomanToIntegerTestsJava
    from app.tests_java.MoneyToEnglishTestsJava import MoneyToEnglishTestsJava
    from app.tests_java.SpiralMatrixTestsJava import SpiralMatrixTestsJava
    from app.tests_java.MedianOfTwoSortedArraysTestsJava import MedianOfTwoSortedArraysTestsJava
    from app.tests_java.LongerValidParenthesesTestsJava import LongerValidParenthesesTestsJava
    from app.tests_java.CountofSmallerNumbersAfterSelfTestsJava import CountSmallerTestsJava
except ImportError as e:
    print(f"Error: Unable to import. {str(e)}")

class CodesControllerJava():
    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name

    def set_up(self):
        if self.name == 'FizzBuzz':
            tests_fizz = FizzBuzzTestsJava()
            return tests_fizz.tests(self.code)
        
        if self.name == 'BinarySearch':
            tests_binary_search = BinarySearchTestsJava()
            return tests_binary_search.tests(self.code)
        
        if self.name == 'Palindrome':
            tests_palindrome = PalindromeTestsJava()
            return tests_palindrome.tests(self.code)
            
        if self.name == 'IntegerToRoman':
            tests_integerToRoman = IntegerToRomanTestsJava()
            return tests_integerToRoman.tests(self.code)
        
        if self.name == 'RomanToInteger':
            tests_romanToInteger = RomanToIntegerTestsJava()
            return tests_romanToInteger.tests(self.code)
        
        if self.name == 'MoneyToEnglish':
            tests_moneyToEnglish = MoneyToEnglishTestsJava()
            return tests_moneyToEnglish.tests(self.code)
        
        if self.name == "SpiralMatrix":
            tests_spiralmatrix =  SpiralMatrixTestsJava()
            return tests_spiralmatrix.tests(self.code)
        
        if self.name == "MedianOfTwoSortedArrays":
            tests_MedianOfTwoSortedArrays = MedianOfTwoSortedArraysTestsJava()
            return tests_MedianOfTwoSortedArrays.tests(self.code)  
        
        if self.name == "LongerValidParentheses":
            tests_LongerValidParentheses = LongerValidParenthesesTestsJava()  
            return tests_LongerValidParentheses.tests(self.code)  
        
        if self.name == "CountofSmallerNumbersAfterSelf":
            tests_CountofSmallerNumbersAfterSelf = CountSmallerTestsJava()  
            return tests_CountofSmallerNumbersAfterSelf.tests(self.code)