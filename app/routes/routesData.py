from flask import Blueprint, jsonify, render_template, request, url_for
try:
    from migrate.db import getResult
except ImportError as e:
    print(f"Error: Unable to import 'migrate.db'. {str(e)}")
    
bp = Blueprint('bp', __name__)

@bp.route('/enviar', methods=['POST'])
def send_code():

    data = request.get_json()

    code_user = data.get('code')
    language = data.get('language')
    problem = data.get('problem')
    resultado = getResult(code_user, language, problem)
    if(language == "csharp"):
        resultado = resultado.text

    return jsonify({"message": resultado}), 201   

@bp.route('/')
def home():
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
            'stars': 3
        },
        {
            'title': 'RomanToInteger',
            'description': 'El algoritmo RomanToInteger convierte números romanos a enteros, analizando los símbolos y aplicando reglas de suma y resta según su posición. Se procesa la cadena de derecha a izquierda para calcular el valor total.',
            'image_url': url_for('static', filename='img/romanToInteger-logo.png'),
            'stars': 3
        },
        {
            'title': 'MoneyToEnglish',
            'description': 'El algoritmo MoneyToEnglish convierte una cantidad monetaria en su representación textual en inglés. Descompone el número en partes enteras y decimales, convirtiendo cada una en palabras para generar una salida clara y correcta.',
            'image_url': url_for('static', filename='img/moneyToEnglish-logo.png'),
            'stars': 4
        },
        {
            'title': 'SpiralMatrix',
            'description': 'Dada una matriz, imprime todos los elementos en orden espiral..',
            'image_url': url_for('static', filename='img/matrix.png'),
            'stars': 5
        },
    ]

    return render_template('index.html', cards=enumerate(cards))

@bp.route('/problems')
def problems():
    value = request.args.get('value', default=None, type=int)
    language = request.args.get('language', default='python')
    problems = [
        {},
        { 
            'title': 'FizzBuzz',
            'problem': 'El objetivo del ejercicio es verificar si un numero dado cumple las condiciones: \n\n Divisibilidad por 3: Si el numero es divisible por 3, devolverás "Fizz". \n\n Divisibilidad por ambos: Si el numero es divisible por 5, devolverás "Buzz". \n\n Divisibilidad por 3: Si el numero es divisible por ambos, devolveras "FizzBuzz". \n\n No es divisible ni por 3 ni por 5: Si el número no es divisible ni por 3 ni por 5, devolverás el número en forma de cadena. \n\n Entrada: n: int : Un número entero (para python) o un numero long (para c#). \n\n Salidas: str: devuelve "Fizz", "Buzz", "FizzBuzz", o el número en forma de cadena.',
            'image_url': url_for('static', filename='img/fizzbuzz-logo.png'),
            'stars': 3,
            "languages": {
                'python': {'code': 'def fizzbuzz(n):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                "c#": {
                    "code": "using TritecAPI.Interfaces;\n\nnamespace TritecAPI.problem_solver\n{\n    public class FizzBuzz : IProblemSolver\n    {\n        public string _fizzBuzz(long number)\n        {\n            //ESCRIBE TU CÓDIGO AQUÍ\n        }\n    }\n}"
                }
            }
        },            
        {
            'title': 'Palindrome',
            'problem': 'El objetivo es verificar si una palabra es palíndromo. Un palíndromo es una palabra que se lee igual de izquierda a derecha y de derecha a izquierda, ignorando los espacios. \n\n Entrada: word: str \n\n Salidas: bool : True si la palabra es palindromo, False en caso contrario.',
            'image_url': url_for('static', filename='img/palindrome-logo.png'),
            'stars': 2,
            'languages': {
                'python': {'code': 'def is_palindrome(word):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'using TritecAPI.Interfaces;\n\nnamespace TritecAPI.problem_solver\n{\n    public class Palindrome\n    {\n        public bool _palindrome(string word)\n        {\n            //ESCRIBE TU CÓDIGO AQUÍ\n        }\n    }\n}'}
            }
        },
        {
            'title': 'BinarySearch',
            'problem': 'Realiza una busqueda binario en un arreglo ordenado para encontrar la posicion de un valor objetivo. \n\n Entrada: arr (Un arreglo ordenado de elementos), target(El valor que se desea encontrar).\n\n Salida: int: El indice del target en el arreglo si se encuentra. En caso contrario, se devuelve -1). ',
            'image_url': url_for('static', filename='img/binary-logo.png'),
            'stars': 2,
            'languages': {
                'python': {'code': 'def binary_search(arr, target):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'using TritecAPI.Interfaces;\n\nnamespace TritecAPI.problem_solver\n{\n    public class BinarySearch\n    {\n        public int _binarySearch(int[] array, int target)\n        {\n            //ESCRIBE TU CÓDIGO AQUÍ\n        }\n    }\n}'}
            }
        },
        {
            'title': 'IntegerToRoman',
            'problem': 'Dada un entero, convierte el número en su representación en números romanos. Los números romanos utilizan combinaciones de letras como I, V, X, L, C, D y M para representar valores. \n\n Entrada: num (Un entero entre 1 y 3999). \n\n Salida: string: La representación en números romanos del entero proporcionado.',
            'image_url': url_for('static', filename='img/integerToRoman-logo.png'),
            'stars': 3,
            'languages': {
                'python': {'code': 'def integer_to_roman(num):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'x'}
            }
        },
        {
            'title': 'RomanToInteger',
            'problem': 'Dada una cadena que representa un número romano, convierte esa cadena en un entero. Los números romanos están compuestos por los siguientes caracteres: I, V, X, L, C, D y M, cada uno de los cuales tiene un valor asociado. Para algunos números romanos, se utilizan combinaciones específicas de estos caracteres para representar valores únicos. \n\n Entrada: s: str (Una cadena que representa un número romano). \n\n Salida: int: La representación entera del número romano proporcionado.',
            'image_url': url_for('static', filename='img/romanToInteger-logo.png'),
            'stars': 3,
            'languages': {
                'python': {'code': 'def roman_to_integer(num):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'x'}
            }
        },
        {
            'title': 'MoneyToEnglish',
            'problem': 'Dada una cantidad de dinero en formato numérico, convierte esa cantidad en su representación en inglés. Por ejemplo, 123.45 debería convertirse en "One Hundred Twenty-Three Dollars and Forty-Five Cents". \n\n Entrada: num: float (Un número que representa la cantidad de dinero). \n\n Salida: str: La representación en inglés de la cantidad de dinero proporcionada.',
            'image_url': url_for('static', filename='img/moneyToEnglish-logo.png'),
            'stars': 4,
            'languages': {
                'python': {'code': 'def money_to_english(num):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'x'}
            }
        },
        {
            'title': 'SpiralMatrix',
            'problem': 'Dada una matriz en el order espiral, es decir desde la esquina superior izquierda, hacia la derecha, luego hacia abajo, luego a la izquierda y finalmente hacia arriba, repitiendo este patrón hasta recorrer toda la matriz \n\n Límites:  Tendremos cuatro "límites" que nos ayudarán a controlar la dirección en la que estamos moviéndonos. (Top, bottom, left, right) ',
            'image_url': url_for('static', filename='img/matrix.png'),
            'stars': 4,
            'languages': {
                'python': {'code': 'def SpiralMatrix(matrix):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'x'}
            }
        },

    ]

    for problem in problems:
        if 'problem' in problem:
            problem['problem'] = problem['problem'].replace('\n', '<br>')

    problem = problems[value] if value is not None and 0 <= value < len(problems) else None

    if problem:
        problem['selected_code'] = problem['languages'].get(language, {}).get('code', '')

    return render_template('problems.html', problem=problem)

@bp.route('/login')
def login():    
    return render_template('login.html')

@bp.route('/register')
def register():    
    return render_template('register.html')