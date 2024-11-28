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
                    "code": "public class FizzBuzz {\n    \n    public static String fizzBuzz(int numero) {\n        if (numero % 3 == 0 && numero % 5 == 0) {\n            return \"FizzBuzz\"; // Si es divisible por 3 y 5, retorna \"FizzBuzz\"\n        } else if (numero % 3 == 0) {\n            return \"Fizz\"; // Si es divisible solo por 3, retorna \"Fizz\"\n        } else if (numero % 5 == 0) {\n            return \"Buzz\"; // Si es divisible solo por 5, retorna \"Buzz\"\n        } else {\n            return Integer.toString(numero); // Si no es divisible ni por 3 ni por 5, retorna el número\n        }\n    }\n}"
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
                'java': {"code": "public class Palindrome {\n    public static boolean isPalindrome(String word) {\n        // Eliminar espacios y convertir a minúsculas\n        word = word.replace(\" \", \"\").toLowerCase();\n        \n        int length = word.length();\n        for (int i = 0; i < length / 2; i++) {\n            if (word.charAt(i) != word.charAt(length - i - 1)) {\n                return false;\n            }\n        }\n        return true;\n    }\n}"}
                
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
                "java": {"code": "public class BinarySearch {\n    public static int binarySearch(int[] arr, int target) {\n        int left = 0, right = arr.length - 1;\n        while (left <= right) {\n            int mid = (left + right) / 2;\n            if (arr[mid] == target) {\n                return mid;\n            } else if (arr[mid] < target) {\n                left = mid + 1;\n            } else {\n                right = mid - 1;\n            }\n        }\n        return -1;\n    }\n}"}
            }
        },
        {
            'id': '3',
            'title': 'IntegerToRoman',
            'problem': '<b>OBJETIVO:</b> \n\n Dada un entero, convierte el número en su representación en números romanos. Los números romanos utilizan combinaciones de letras como I, V, X, L, C, D y M para representar valores. \n\n <b>Entrada:</b>: num (Un entero entre 1 y 3999). \n\n <b>Salida:</b>: string: La representación en números romanos del entero proporcionado. \n\n <b>Ejemplo:</b> \n\n <b>Entrada:</b>: \"56\" \n\n <b>Salida:</b> = LVI \n\n <b>Explicacion:</b> = El número 56 se representa como LVI en números romanos, donde L es 50, V es 5 e I es 1. Por lo tanto, 50 + 5 + 1 = 56. ',
            'image_url': url_for('static', filename='img/integerToRoman-logo.png'),
            'stars': 3,
            'languages': {
                'python': {'code': 'def integer_to_roman(num):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'x'},
                'java': {"code": "public class IntegerToRoman {\n    public static String integerToRoman(int num) {\n        // Arreglo con los valores de los números romanos\n        int[] val = {\n            1000, 900, 500, 400,\n            100, 90, 50, 40,\n            10, 9, 5, 4,\n            1\n        };\n\n        // Arreglo con los símbolos correspondientes a cada valor\n        String[] syms = {\n            \"M\", \"CM\", \"D\", \"CD\",\n            \"C\", \"XC\", \"L\", \"XL\",\n            \"X\", \"IX\", \"V\", \"IV\",\n            \"I\"\n        };\n\n        // Cadena para almacenar el resultado\n        StringBuilder romanNum = new StringBuilder();\n\n        // Iterar sobre los valores romanos\n        for (int i = 0; i < val.length; i++) {\n            // Mientras el número sea mayor que el valor actual\n            while (num >= val[i]) {\n                romanNum.append(syms[i]);  // Añadir el símbolo correspondiente\n                num -= val[i];             // Restar el valor de num\n            }\n        }\n\n        return romanNum.toString();\n    }\n}"}
            }
        },
        {
            'id': '4',
            'title': 'RomanToInteger',
            'problem': '<b>OBJETIVO:</b> \n\n Dada una cadena que representa un número romano, convierte esa cadena en un entero. Los números romanos están compuestos por los siguientes caracteres: I, V, X, L, C, D y M, cada uno de los cuales tiene un valor asociado. Para algunos números romanos, se utilizan combinaciones específicas de estos caracteres para representar valores únicos. \n\n <b>Entrada:</b>: s: str (Una cadena que representa un número romano). \n\n <b>Salida:</b>: int: La representación entera del número romano proporcionado. \n\n <b>Ejemplo:</b> \n\n <b>Entrada:</b>: \"IX\" \n\n <b>Salida:</b> = 9 \n\n <b>Explicacion:</b> = l número romano '"IX"' representa el valor 9, ya que '"I"' es 1 y '"X"' es 10, y dado que '"I"' precede a '"x"', el valor total es 10 - 1 = 9.',
            'image_url': url_for('static', filename='img/romanToInteger-logo.png'),
            'stars': 3,
            'languages': {
                'python': {'code': 'def roman_to_integer(num):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'x'},
                'java': {"code": "import java.util.HashMap;\nimport java.util.Map;\n\npublic class RomanToInteger {\n    public static int romanToInteger(String num) {\n        // Crear un mapa de los valores de los números romanos\n        Map<Character, Integer> romanNumerals = new HashMap<>();\n        romanNumerals.put('I', 1);\n        romanNumerals.put('V', 5);\n        romanNumerals.put('X', 10);\n        romanNumerals.put('L', 50);\n        romanNumerals.put('C', 100);\n        romanNumerals.put('D', 500);\n        romanNumerals.put('M', 1000);\n\n        int total = 0;\n        int prevValue = 0;\n\n        // Recorrer el número romano de derecha a izquierda\n        for (int i = num.length() - 1; i >= 0; i--) {\n            char currentChar = num.charAt(i);\n            int value = romanNumerals.get(currentChar);\n\n            // Si el valor actual es menor que el valor anterior, restamos, sino sumamos\n            if (value < prevValue) {\n                total -= value;\n            } else {\n                total += value;\n            }\n\n            prevValue = value;  // Actualizamos el valor anterior\n        }\n\n        return total;\n    }\n}"}
            }
        },
        {
            'id': '5',
            'title': 'MoneyToEnglish',
            'problem': '<b>OBJETIVO:</b> \n\n Dada una cantidad de dinero en formato numérico, convierte esa cantidad en su representación en inglés. Por ejemplo, 123.45 debería convertirse en "One Hundred Twenty-Three Dollars and Forty-Five Cents". \n\n <b>Entrada:</b>: num: float (Un número que representa la cantidad de dinero). \n\n <b>Salida:</b>: str: La representación en inglés de la cantidad de dinero proporcionada.\n\n <b>Ejemplo:</b> \n\n <b>Entrada:</b>: \"10\" \n\n <b>Salida:</b> = ten \n\n <b>Explicacion:</b> = La traduccion directa de 10 en ingles es "Ten" ',
            'image_url': url_for('static', filename='img/moneyToEnglish-logo.png'),
            'stars': 4,
            'languages': {
                'python': {'code': 'def money_to_english(num):\n\n    #ESCRIBE TU CÓDIGO AQUÍ'},
                'c#': {'code': 'x'},
                'java': {"code": "public class MoneyToEnglish {\n    \n    public static String moneyToEnglish(double num) {\n        if (num < 0) {\n            return \"negative \" + moneyToEnglish(-num);\n        }\n\n        // Arrays con las palabras correspondientes\n        String[] units = {\"\", \"one\", \"two\", \"three\", \"four\", \"five\", \"six\", \"seven\", \"eight\", \"nine\"};\n        String[] teens = {\"ten\", \"eleven\", \"twelve\", \"thirteen\", \"fourteen\", \"fifteen\", \n                          \"sixteen\", \"seventeen\", \"eighteen\", \"nineteen\"};\n        String[] tens = {\"\", \"\", \"twenty\", \"thirty\", \"forty\", \"fifty\", \"sixty\", \"seventy\", \"eighty\", \"ninety\"};\n\n        // Si el número es 0\n        if (num == 0) {\n            return \"zero dollars\";\n        }\n\n        // Separar la parte de los dólares y los centavos\n        int dollars = (int) num;\n        int cents = (int) Math.round((num - dollars) * 100);\n\n        StringBuilder words = new StringBuilder();\n\n        // Convertir dólares a palabras\n        if (dollars >= 1000) {\n            words.append(units[dollars / 1000]).append(\" thousand \");\n            dollars %= 1000;\n        }\n\n        if (dollars >= 100) {\n            words.append(units[dollars / 100]).append(\" hundred \");\n            dollars %= 100;\n        }\n\n        if (dollars >= 20) {\n            words.append(tens[dollars / 10]).append(\" \");\n            dollars %= 10;\n        }\n\n        if (dollars >= 10) {\n            words.append(teens[dollars - 10]).append(\" \");\n            dollars = 0;\n        }\n\n        if (dollars > 0) {\n            words.append(units[dollars]).append(\" \");\n        }\n\n        // Agregar \"dollar\" o \"dollars\"\n        String dollarWords = words.toString().trim() + (words.toString().trim().equals(\"one\") ? \" dollar\" : \" dollars\");\n\n        // Si hay centavos, convertirlos a palabras\n        if (cents > 0) {\n            words.setLength(0); // Limpiar el StringBuilder para los centavos\n\n            if (cents >= 20) {\n                words.append(tens[cents / 10]).append(\" \");\n                cents %= 10;\n            }\n\n            if (cents >= 10) {\n                words.append(teens[cents - 10]).append(\" \");\n                cents = 0;\n            }\n\n            if (cents > 0) {\n                words.append(units[cents]).append(\" \");\n            }\n\n            // Agregar \"cent\" o \"cents\"\n            String centWords = words.toString().trim() + (words.toString().trim().equals(\"one\") ? \" cent\" : \" cents\");\n            return dollarWords + \" and \" + centWords;\n        }\n\n        return dollarWords;\n    }\n}"}
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
                'c#': {'code': 'x'},
                'java': {"code": "import java.util.ArrayList;\nimport java.util.List;\n\npublic class SpiralMatrix {\n    public static List<Integer> spiralMatrix(int[][] matrix) {\n        List<Integer> result = new ArrayList<>();\n        \n        // Verificar si la matriz está vacía\n        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {\n            return result;\n        }\n\n        int top = 0, bottom = matrix.length - 1;\n        int left = 0, right = matrix[0].length - 1;\n\n        while (top <= bottom && left <= right) {\n            // Recorrer de izquierda a derecha en la fila superior\n            for (int i = left; i <= right; i++) {\n                result.add(matrix[top][i]);\n            }\n            top++;\n\n            // Recorrer de arriba a abajo en la columna derecha\n            for (int i = top; i <= bottom; i++) {\n                result.add(matrix[i][right]);\n            }\n            right--;\n\n            // Recorrer de derecha a izquierda en la fila inferior (si aún es válida)\n            if (top <= bottom) {\n                for (int i = right; i >= left; i--) {\n                    result.add(matrix[bottom][i]);\n                }\n                bottom--;\n            }\n\n            // Recorrer de abajo a arriba en la columna izquierda (si aún es válida)\n            if (left <= right) {\n                for (int i = bottom; i >= top; i--) {\n                    result.add(matrix[i][left]);\n                }\n                left++;\n            }\n        }\n\n        return result;\n    }\n}"}
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
                'c#': {'code': 'x'},
                'java': {"code": "import java.util.ArrayList;\nimport java.util.Arrays;\nimport java.util.List;\n\npublic class MedianOfTwoSortedArrays {\n    public static double medianOfTwoSortedArrays(int[] array1, int[] array2) {\n        // Crear una lista para combinar ambos arrays\n        int[] combinedArray = new int[array1.length + array2.length];\n        \n        // Copiar los elementos de ambos arrays a la lista combinada\n        System.arraycopy(array1, 0, combinedArray, 0, array1.length);\n        System.arraycopy(array2, 0, combinedArray, array1.length, array2.length);\n        \n        // Ordenar el array combinado\n        Arrays.sort(combinedArray);\n        \n        // Calcular el tamaño del array combinado\n        int size = combinedArray.length;\n        \n        // Si el tamaño es impar, la mediana es el valor del medio\n        if (size % 2 == 1) {\n            return combinedArray[size / 2];\n        } else {\n            // Si el tamaño es par, la mediana es el promedio de los dos valores centrales\n            return (combinedArray[size / 2 - 1] + combinedArray[size / 2]) / 2.0;\n        }\n    }\n}"}
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
                'c#': {'code': 'x'},
                'java': {"code": "import java.util.Stack;\n\npublic class LongerValidParentheses {\n    public static int longerValidParentheses(String s) {\n        Stack<Integer> stack = new Stack<>();\n        stack.push(-1);  // Agregar un marcador inicial para manejar casos como \"()\"\n\n        int maxLength = 0;\n\n        for (int i = 0; i < s.length(); i++) {\n            char charAt = s.charAt(i);\n\n            if (charAt == '(') {\n                // Coloca el índice del paréntesis de apertura en la pila\n                stack.push(i);\n            } else if (charAt == ')') {\n                // Desapilar el índice del paréntesis de apertura correspondiente\n                stack.pop();\n\n                // Si la pila no está vacía, calcular la longitud del paréntesis válido\n                if (!stack.isEmpty()) {\n                    maxLength = Math.max(maxLength, i - stack.peek());\n                } else {\n                    // Si la pila está vacía, agregamos el índice actual como marcador base\n                    stack.push(i);\n                }\n            }\n        }\n\n        return maxLength/2;\n    }\n}"}
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
                'c#': {'code': 'x'},
                'java': {"code": "public class CountSmaller {\n    public static int[] countSmaller(int[] nums) {\n        int[] counts = new int[nums.length];\n        \n        for (int i = 0; i < nums.length; i++) {\n            for (int j = i + 1; j < nums.length; j++) {\n                if (nums[j] < nums[i]) {\n                    counts[i]++;\n                }\n            }\n        }\n        \n        return counts;\n    }\n}"}
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
    print(codes)
    return render_template('codesSubmits.html', value=value, codes=codes)
