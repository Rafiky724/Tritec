from flask import Blueprint, jsonify, render_template, request, url_for, session
from ..models.models import User, Codes
from functools import wraps
try:
    from migrate.db import getResult
except ImportError as e:
    print(f"Error: Unable to import 'migrate.db'. {str(e)}")
    
bp = Blueprint('bp', __name__)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return render_template('login.html')
    return wrap

@bp.route('/enviar', methods=['POST'])
@login_required
def send_code():

    data = request.get_json()

    code_user = data.get('code')
    language = data.get('language')
    problem = data.get('problem')
    resultado = getResult(code_user, language, problem)
    """
    if(language == "csharp"):
        resultado = resultado.text"""

    return jsonify({"message": resultado}), 201   

@bp.route('/')
@login_required
def home():
    user_exercise = session['user']['exercise']

    cards = [
        {},
        {
            'title': 'FizzBuzz',
            'description': 'El problema de FizzBuzz consiste en reemplazar los números de una lista con "Fizz" si son múltiplos de 3, "Buzz" si son múltiplos de 5, y "FizzBuzz" si son múltiplos de ambos.',
            'image_url': url_for('static', filename='img/fizzbuzz-logo.png'),
            'stars': 3
        },
        {
            'title': 'Palindrome',
            'description': 'El algoritmo para verificar si una palabra es un palíndromo normaliza la entrada eliminando espacios y convirtiendo todas las letras a minúsculas. Luego, compara la palabra resultante con su versión invertida. Si ambas versiones son iguales, la palabra es un palíndromo; de lo contrario, no lo es.',
            'image_url': url_for('static', filename='img/palindrome-logo.png'),
            'stars': 2
        },
        {
            'title': 'BinarySearch',
            'description': 'El algoritmo de Binary Search busca un elemento en una lista ordenada dividiendo repetidamente el rango de búsqueda a la mitad, comparando el elemento buscado con el valor en el punto medio, y ajustando el rango según corresponda.',
            'image_url': url_for('static', filename='img/binary-logo.png'),
            'stars': 2
        },
        {
            'title': 'IntegerToRoman',
            'description': 'El algoritmo de Integer to Roman convierte un número entero a su representación en números romanos utilizando un enfoque de resta. Se utilizan listas de valores y símbolos romanos para formar la representación correcta a partir de la entrada numérica.',
            'image_url': url_for('static', filename='img/integerToRoman-logo.png'),
            'stars': 4
        },
        {
            'title': 'RomanToInteger',
            'description': 'El algoritmo RomanToInteger convierte números romanos a enteros, analizando los símbolos y aplicando reglas de suma y resta según su posición. Se procesa la cadena de derecha a izquierda para calcular el valor total.',
            'image_url': url_for('static', filename='img/romanToInteger-logo.png'),
            'stars': 4
        },
        {
            'title': 'MoneyToEnglish',
            'description': 'El algoritmo MoneyToEnglish convierte una cantidad monetaria en su representación textual en inglés. Descompone el número en partes enteras y decimales, convirtiendo cada una en palabras para generar una salida clara y correcta.',
            'image_url': url_for('static', filename='img/moneyToEnglish-logo.png'),
            'stars': 5
        },
        {
            'title': 'SpiralMatrix',
            'description': 'El problema de "Spiral Matrix" consiste en, dada una matriz de enteros de dimensiones m x n (donde m es el número de filas y n es el número de columnas), imprimir los elementos de la matriz en un orden espiral',
            'image_url': url_for('static', filename='img/spiral-logo.png'),
            'stars': 4
        },
        {
            'title': 'MedianOfTwoSortedArrays',
            'description': "'El problema de \"Median of Two Sorted Arrays\" consiste en, dadas dos matrices ordenadas, nums1 y nums2 de tamaño m y n respectivamente, devolver la mediana de las dos matrices ordenadas. La mediana es el valor que separa la mitad superior de la mitad inferior de los elementos cuando las dos matrices se combinan y se ordenan.'",
            'image_url': url_for('static', filename='img/median-logo.png'),
            'stars': 2
        },
        {
            'title': 'LongerValidParentheses',
            'description': "'El problema de \"Longer valid parentheses\" consiste Dada una cadena que contiene solo los caracteres '(' y ')', devuelve la longitud del paréntesis válido más largo'",
            'image_url': url_for('static', filename='img/parentheses-logo.png'),
            'stars': 3
        },
        {
            'title': 'CountofSmallerNumbersAfterSelf',
            'description': "'El problema de \"Count of Smaller Numbers After Self\" Consistes en dada una matriz con numeros enteros, se debera devolver una matriz de enteros donde sus elementos sean el numero de elemenentos mas pequeños a la derecha de nums[i]'",
            'image_url': url_for('static', filename='img/count-logo.png'),
            'stars': 1
        },

    ]

    
    for i, card in enumerate(cards):
        if i != 0:
            card['status'] = user_exercise[i-1]
    

    return render_template('index.html', cards=enumerate(cards))

@bp.route('/problems')
@login_required
def problems():
    value = request.args.get('value', default=None, type=int)
    language = request.args.get('language', default='python')
    problems = [
        {},
        { 
            'id': '0',
            'title': 'FizzBuzz',
            'problem': '<b>OBJETIVO:</b> \n\n El objetivo del ejercicio es verificar si un numero dado cumple las condiciones: \n\n Divisibilidad por 3: Si el numero es divisible por 3, devolverás "Fizz". \n\n Divisibilidad por ambos: Si el numero es divisible por 5, devolverás "Buzz". \n\n Divisibilidad por 3: Si el numero es divisible por ambos, devolveras "FizzBuzz". \n\n No es divisible ni por 3 ni por 5: Si el número no es divisible ni por 3 ni por 5, devolverás el número en forma de cadena. \n\n <b>Entrada:</b>: n: int : Un número entero (para python) o un numero long (para c#). \n\n <b>Salida:</b>: str: devuelve "Fizz", "Buzz", "FizzBuzz", o el número en forma de cadena. \n\n <b>Ejemplo:</b> \n\n <b>Entrada:</b> n = 15 \n\n <b>Salida:</b> = FizzBuzz \n\n <b>Explicacion:</b> = En este caso, 15 es divisible tanto por 3 como por 5, por lo que la salida es "FizzBuzz".',
            'image_url': url_for('static', filename='img/fizzbuzz-logo.png'),
            'stars': 3,
            "languages": {
                'python': {'code': 'def fizzbuzz(n):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                "c#": {
                    "code": "using TritecAPI.Interfaces;\n\nnamespace TritecAPI.problem_solver\n{\n    public class FizzBuzz : IProblemSolver\n    {\n        public string _fizzBuzz(long number)\n        {\n            //ESCRIBE TU CÓDIGO AQUÍ\n        }\n    }\n}"
                },
                "java": {
                    "code": "public class FizzBuzz {\n    \n    public static String fizzBuzz(int numero) {\n            //ESCRIBE TU CÓDIGO AQUÍ    }\n}"
                }
            }
        },            
        {
            'id': '1',
            'title': 'Palindrome',
            'problem': '<b>OBJETIVO:</b> \n\n El objetivo es verificar si una palabra es palíndromo. Un palíndromo es una palabra que se lee igual de izquierda a derecha y de derecha a izquierda, ignorando los espacios. \n\n <b>Entrada:</b>: word: str \n\n <b>Salida:</b>: bool : True si la palabra es palindromo, False en caso contrario. \n\n <b>Ejemplo:</b> \n\n <b>Entrada:</b>: \"anita lava la tina\" \n\n <b>Salida:</b> = True \n\n <b>Explicacion:</b> = La frase \"anita lava la tina\" es un palíndromo porque se lee igual de izquierda a derecha que de derecha a izquierda, ignorando los espacios. ',
            'image_url': url_for('static', filename='img/palindrome-logo.png'),
            'stars': 2,
            'languages': {
                'python': {'code': 'def is_palindrome(word):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'using TritecAPI.Interfaces;\n\nnamespace TritecAPI.problem_solver\n{\n    public class Palindrome\n    {\n        public bool _palindrome(string word)\n        {\n            //ESCRIBE TU CÓDIGO AQUÍ\n        }\n    }\n}'},
                'java': {"code": "public class Palindrome {\n    public static boolean isPalindrome(String word) {\n            //ESCRIBE TU CÓDIGO AQUÍ    }\n}"}
                
            }
        },
        {
            'id': '2',
            'title': 'BinarySearch',
            'problem': '<b>OBJETIVO:</b> \n\n Realiza una busqueda binario en un arreglo ordenado para encontrar la posicion de un valor objetivo. \n\n <b>Entrada:</b>: arr (Un arreglo ordenado de elementos), target(El valor que se desea encontrar).\n\n <b>Salida:</b>: int: El indice del target en el arreglo si se encuentra. En caso contrario, se devuelve -1). \n\n <b>Ejemplo:</b> \n\n <b>Entrada:</b>: arr = [1, 3, 5, 7, 9, 11], target = 7 \n\n <b>Salida:</b> = 3 \n\n <b>Explicacion:</b> = El valor 7 se encuentra en la posicion 3 del arreglo  ',
            'image_url': url_for('static', filename='img/binary-logo.png'),
            'stars': 2,
            'languages': {
                'python': {'code': 'def binary_search(arr, target):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'using TritecAPI.Interfaces;\n\nnamespace TritecAPI.problem_solver\n{\n    public class BinarySearch\n    {\n        public int _binarySearch(int[] array, int target)\n        {\n            //ESCRIBE TU CÓDIGO AQUÍ\n        }\n    }\n}'},
                "java": {"code": "public class BinarySearch {\n    public static int binarySearch(int[] arr, int target) {\n            //ESCRIBE TU CÓDIGO AQUÍ    }\n}"}
            }
        },
        {
            'id': '3',
            'title': 'IntegerToRoman',
            'problem': '<b>OBJETIVO:</b> \n\n Dada un entero, convierte el número en su representación en números romanos. Los números romanos utilizan combinaciones de letras como I, V, X, L, C, D y M para representar valores. \n\n <b>Entrada:</b>: num (Un entero entre 1 y 3999). \n\n <b>Salida:</b>: string: La representación en números romanos del entero proporcionado. \n\n <b>Ejemplo:</b> \n\n <b>Entrada:</b>: \"56\" \n\n <b>Salida:</b> = LVI \n\n <b>Explicacion:</b> = El número 56 se representa como LVI en números romanos, donde L es 50, V es 5 e I es 1. Por lo tanto, 50 + 5 + 1 = 56. ',
            'image_url': url_for('static', filename='img/integerToRoman-logo.png'),
            'stars': 4,
            'languages': {
                'python': {'code': 'def integer_to_roman(num):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'using System.Text;\n\n namespace TritecAPI.problem_solver\n{\n    public class integerToRoman\n    {\n        public string _intToRoman(int num)\n {\n            //ESCRIBE TU CÓDIGO AQUÍ\n        }\n    }\n}'},
                'java': {"code": "public class IntegerToRoman {\n    public static String integerToRoman(int num) {\n            //ESCRIBE TU CÓDIGO AQUÍ    }\n}"}
            }
        },
        {
            'id': '4',
            'title': 'RomanToInteger',
            'problem': '<b>OBJETIVO:</b> \n\n Dada una cadena que representa un número romano, convierte esa cadena en un entero. Los números romanos están compuestos por los siguientes caracteres: I, V, X, L, C, D y M, cada uno de los cuales tiene un valor asociado. Para algunos números romanos, se utilizan combinaciones específicas de estos caracteres para representar valores únicos. \n\n <b>Entrada:</b>: s: str (Una cadena que representa un número romano). \n\n <b>Salida:</b>: int: La representación entera del número romano proporcionado. \n\n <b>Ejemplo:</b> \n\n <b>Entrada:</b>: \"IX\" \n\n <b>Salida:</b> = 9 \n\n <b>Explicacion:</b> = l número romano '"IX"' representa el valor 9, ya que '"I"' es 1 y '"X"' es 10, y dado que '"I"' precede a '"x"', el valor total es 10 - 1 = 9.',
            'image_url': url_for('static', filename='img/romanToInteger-logo.png'),
            'stars': 4,
            'languages': {
                'python': {'code': 'def roman_to_integer(num):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'using System.Collections.Generic;;\n\nnamespace TritecAPI.problem_solver\n{\n    public class RomanToInteger \n    {\n        public string _romanToInt(string s)\n {\n            //ESCRIBE TU CÓDIGO AQUÍ\n        }\n    }\n}'},
                'java': {"code": "import java.util.HashMap;\nimport java.util.Map;\n\npublic class RomanToInteger {\n    public static int romanToInteger(String num) {\n            //ESCRIBE TU CÓDIGO AQUÍ    }\n}"}
            }
        },
        {
            'id': '5',
            'title': 'MoneyToEnglish',
            'problem': '<b>OBJETIVO:</b> \n\n Dada una cantidad de dinero en formato numérico, convierte esa cantidad en su representación en inglés. Por ejemplo, 123.45 debería convertirse en "One Hundred Twenty-Three Dollars and Forty-Five Cents". \n\n <b>Entrada:</b>: num: float (Un número que representa la cantidad de dinero). \n\n <b>Salida:</b>: str: La representación en inglés de la cantidad de dinero proporcionada.\n\n <b>Ejemplo:</b> \n\n <b>Entrada:</b>: \"10\" \n\n <b>Salida:</b> = ten \n\n <b>Explicacion:</b> = La traduccion directa de 10 en ingles es "Ten" ',
            'image_url': url_for('static', filename='img/moneyToEnglish-logo.png'),
            'stars': 5,
            'languages': {
                'python': {'code': 'def money_to_english(num):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'using System;\n\nnamespace TritecAPI.problem_solver\n{\n    public class MoneyToEnglish \n    {\n        private static readonly string[] Ones = new string[] { "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" }; \n private static readonly string[] Tens = new string[] { "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" }; \n private static readonly string[] Thousands = new string[] { "", "thousand", "million", "billion" };\n  public string ConvertToWords(decimal number) \n {\n            //ESCRIBE TU CÓDIGO AQUÍ\n        }\n    }\n}'},
                'java': {"code": "public class MoneyToEnglish {\n    \n    public static String moneyToEnglish(double num) {\n            //ESCRIBE TU CÓDIGO AQUÍ    }\n}"}
            }
        },
        {
            'id': '6',
            'title': 'SpiralMatrix',
            'problem': '<b>OBJETIVO:</b> \n\n El objetivo de El recorrido debe comenzar desde la esquina superior izquierda y seguir un patrón espiral, recorriendo la matriz de manera secuencial a lo largo de sus bordes y luego hacia el interior, hasta que todos los elementos hayan sido impresos. \n\n <b>Ejemplo:</b> \n\n <b>Entrada:</b> \n\n [[1,2,3], \n [4,5,6], \n [7,8,9]] \n\n <b>Salida:</b>: [1, 2, 3, 6, 9, 8, 7, 4, 5] ',
            'image_url': url_for('static', filename='img/spiral-logo.png'),
            'stars': 4,
            'languages': {
                'python': {'code': 'def spiralmatrix(matrix):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'using System; \n\nusing System.Collections.Generic; \n\nnamespace TritecAPI.problem_solver\n{\n    public class SpiralMatrix \n    {\n        public string _romanToInt(string s)\n {\n            //ESCRIBE TU CÓDIGO AQUÍ\n        }\n    }\n}'},
                'java': {"code": "import java.util.ArrayList;\nimport java.util.List;\n\npublic class SpiralMatrix {\n    public static List<Integer> spiralMatrix(int[][] matrix) {\n            //ESCRIBE TU CÓDIGO AQUÍ    }\n}"}
            }
        },
        {
            'id': '7',
            'title': 'MedianOfTwoSortedArrays',
            'problem': '<b>OBJETIVO:</b> \n\n El objetivo es que dado dos arreglos ordenados nums1 y nums2, el objetivo es encontrar la mediana de la combinación de ambos sin fusionarlos completamente. La solución eficiente utiliza búsqueda binaria en el arreglo más pequeño para dividir ambos arreglos en dos subarreglos de tal manera que la cantidad de elementos a la izquierda de la división sea igual (o casi igual, si el total es impar). Asegurándose de que los elementos de la mitad izquierda sean menores que los de la mitad derecha, se calcula la mediana.',
            'image_url': url_for('static', filename='img/median-logo.png'),
            'stars': 2,
            'languages': {
                'python': {'code': 'def median_of_two_sorted_arrays(array1, array2):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'using System;\n\nnamespace TritecAPI.problem_solver\n{\n    public class MedianOfTwoSortedArrays \n {\n        public double FindMedianSortedArrays(int[] nums1, int[] nums2)\n {\n            //ESCRIBE TU CÓDIGO AQUÍ\n        }\n    }\n}'},
                'java': {"code": "import java.util.ArrayList;\nimport java.util.Arrays;\nimport java.util.List;\n\n    public class MedianOfTwoSortedArrays {\n    public static double medianOfTwoSortedArrays(int[] array1, int[] array2) {\n            //ESCRIBE TU CÓDIGO AQUÍ    }\n}"}
            }
        },
        {
            'id': '8',
            'title': 'LongerValidParentheses',
            'problem': '<b>OBJETIVO:</b> \n\n Dado la cadena que contiene caracteres parentesis, el objetivo es encontrar la maxima cantidad de parentesis correctamente cerrados \n\n <b>Ejemplo:</b> \n\n <b>Entrada:</b>: s = = ")()())" \n\n <b>Salida:</b>: 2 \n\n Explicación: La cantidad de parentesis válida es "La subcadena de paréntesis válida más larga es "()()". <b>Ejemplo:</b> \n\n<b>Entrada:</b> nums1 = [1, 3], nums2 = [2] <br> \n\n <b>Salida:</b> 2.0 <br><br \n\n <b>Explicacion:</b>: Los dos arreglos combinados son [1, 2, 3]. La mediana es el valor en el medio, que es 2.',
            'image_url': url_for('static', filename='img/parentheses-logo.png'),
            'stars': 3,
            'languages': {
                'python': {'code': 'def longer_valid_parentheses(s):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'using System; \n\nusing System.Collections.Generic; \n\nnamespace TritecAPI.problem_solver\n{\n    public int LongestValidParentheses \n    {\n        public int LongestValidParentheses(string s) \n {\n            //ESCRIBE TU CÓDIGO AQUÍ\n        }\n    }\n}'},
                'java': {"code": "import java.util.Stack;\n\npublic class LongerValidParentheses {\n    public static int longerValidParentheses(String s) {\n            //ESCRIBE TU CÓDIGO AQUÍ    }\n}"}
            }
        },
        {
            'id': '9',
            'title': 'CountofSmallerNumbersAfterSelf',
            'problem': '<b>OBJETIVO:</b> \n\n Este problema se refiere a contar cuántos elementos a la derecha de un número son más pequeños que ese número. La idea es iterar a través del arreglo y para cada elemento contar cuántos números a la derecha son menores que el número actual. \n\n <b>Ejemplo:</b> \n\n <b>Entrada:</b>: nums = [5,2,6,1] \n\n <b>Salida:</b>: [2,1,1,0] \n\n <b>Explicacion:</b>: A la derecha de 5 hay 2 elementos más pequeños (2 y 1). \n\n' ,
            'image_url': url_for('static', filename='img/count-logo.png'),
            'stars': 1,
            'languages': {
                'python': {'code': 'def count_Smaller(nums):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'using System; \n\nusing System.Collections.Generic; \n\nnamespace TritecAPI.problem_solver\n{\n    public class CountofSmallerNumbersAfterSelf \n    {\n        public int[] CountSmaller(int[] nums)\n {\n            //ESCRIBE TU CÓDIGO AQUÍ\n        }\n    }\n}'},
                'java': {"code": "public class CountSmaller {\n    public static int[] countSmaller(int[] nums) {\n            //ESCRIBE TU CÓDIGO AQUÍ    }\n}"}
            }
        },

    ]

    for problem in problems:
        if 'problem' in problem:
            problem['problem'] = problem['problem'].replace('\n', '<br>')

    problem = problems[value] if value is not None and 0 <= value < len(problems) else None

    if problem:
        problem['selected_code'] = problem['languages'].get(language, {}).get('code', '')

    return render_template('problems.html', problem=problem, value=value)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return User().login()
    else:
        return render_template('login.html')
    
@bp.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        user = User()
        return user.register()

    return render_template('register.html')

@bp.route('/signout', methods=['GET'])
@login_required
def signout():
    return User().signout()

@bp.route('/submit', methods=['POST'])
@login_required
def submitCode():
    data = request.get_json()
    if data['value']:
        User().update_exercise(str(data.get('id')))

    Codes().submit_code(data)
    
    return data

@bp.route('/submits')
@login_required
def submits():

    value = request.args.get('value', default=None, type=int)
    
    codes = list(Codes().get_codes(value))
    #print(codes)
    return render_template('codesSubmits.html', value=value, codes=codes)


@bp.route('/user')
@login_required
def user():
    user_exercise = session['user']['exercise']
    
    problems = [
        { 
            'id': '0',
            'title': 'FizzBuzz',
            'image_url': url_for('static', filename='img/fizzbuzz-logo.png'),
            'like': url_for('static', filename='img/complete.png'),
            'dislike': url_for('static', filename='img/uncomplete.png'),
        },            
        {
            'id': '1',
            'title': 'Palindrome',
            'image_url': url_for('static', filename='img/palindrome-logo.png'),
            'like': url_for('static', filename='img/complete.png'),
            'dislike': url_for('static', filename='img/uncomplete.png'),
        },
        {
            'id': '2',
            'title': 'BinarySearch',
            'image_url': url_for('static', filename='img/binary-logo.png'),
            'like': url_for('static', filename='img/complete.png'),
            'dislike': url_for('static', filename='img/uncomplete.png'),
        },
        {
            'id': '3',
            'title': 'IntegerToRoman',
            'image_url': url_for('static', filename='img/integerToRoman-logo.png'),
            'like': url_for('static', filename='img/complete.png'),
            'dislike': url_for('static', filename='img/uncomplete.png'),
        },
        {
            'id': '4',
            'title': 'RomanToInteger',
            'image_url': url_for('static', filename='img/romanToInteger-logo.png'),
            'like': url_for('static', filename='img/complete.png'),
            'dislike': url_for('static', filename='img/uncomplete.png'),
        },
        {
            'id': '5',
            'title': 'MoneyToEnglish',
            'image_url': url_for('static', filename='img/moneyToEnglish-logo.png'),
            'like': url_for('static', filename='img/complete.png'),
            'dislike': url_for('static', filename='img/uncomplete.png'),
        },
        {
            'id': '6',
            'title': 'SpiralMatrix',
            'image_url': url_for('static', filename='img/spiral-logo.png'),
            'like': url_for('static', filename='img/complete.png'),
            'dislike': url_for('static', filename='img/uncomplete.png'),
        },
        {
            'id': '7',
            'title': 'MedianOfTwoSortedArrays',
            'image_url': url_for('static', filename='img/median-logo.png'),
            'like': url_for('static', filename='img/complete.png'),
            'dislike': url_for('static', filename='img/uncomplete.png'),
        },
        {
            'id': '8',
            'title': 'LongerValidParentheses',
            'image_url': url_for('static', filename='img/parentheses-logo.png'),
            'like': url_for('static', filename='img/complete.png'),
            'dislike': url_for('static', filename='img/uncomplete.png'),
        },
        {
            'id': '9',
            'title': 'CountofSmallerNumbersAfterSelf',
            'image_url': url_for('static', filename='img/count-logo.png'),
            'like': url_for('static', filename='img/complete.png'),
            'dislike': url_for('static', filename='img/uncomplete.png'),
        },

    ]

    for i, problem in enumerate(problems):
        if i >= 0: 
            if user_exercise[i]:  
                problem['status'] = problem['like']
                problem['verify'] = 'Completado'
            else:
                problem['status'] = problem['dislike']
                problem['verify'] = 'No Completado'
    user = User().get_user()
    return render_template('settings.html', cards=problems, user=user)