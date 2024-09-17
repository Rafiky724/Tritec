from flask import Blueprint, jsonify, render_template, request, url_for

from migrate.db import getResult

bp = Blueprint('bp', __name__)

@bp.route('/enviar', methods=['POST'])
def send_code():

    data = request.get_json()

    code_user = data.get('code')
    language = data.get('language')
    problem = data.get('problem')
    
    resultado = getResult(code_user, language, problem)
    print(resultado)

    #return resultado

    #C#
    return jsonify({"message": resultado}), 201
    #return jsonify({"code": code_user, "languaje": language, "problem": problem}), 201

@bp.route('/')
def home():
    cards = [
        {},
        {
            'title': 'FizzBuzz',
            'description': 'El problema de FizzBuzz consiste en reemplazar los números de una lista con "Fizz" si son múltiplos de 3, "Buzz" si son múltiplos de 5, y "FizzBuzz" si son múltiplos de ambos.',
            'image_url': url_for('static', filename='img/fizzbuzz-logo.png'),
            'stars': 5
        },
        {
            'title': 'Palindrome',
            'description': 'El algoritmo para verificar si una palabra es un palíndromo normaliza la entrada eliminando espacios y convirtiendo todas las letras a minúsculas. Luego, compara la palabra resultante con su versión invertida. Si ambas versiones son iguales, la palabra es un palíndromo; de lo contrario, no lo es.',
            'image_url': url_for('static', filename='img/buble-logo.png'),
            'stars': 3
        },
        {
            'title': 'BinarySearch',
            'description': 'El algoritmo de Binary Search busca un elemento en una lista ordenada dividiendo repetidamente el rango de búsqueda a la mitad, comparando el elemento buscado con el valor en el punto medio, y ajustando el rango según corresponda.',
            'image_url': url_for('static', filename='img/binary-logo.png'),
            'stars': 4
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
            'problem': 'El objetivo del ejercicio es verificar si un numero dado cumple las condiciones: \n Divisibilidad por 3: Si el numero es divisible por 3, devolveras "Fizz" \n Divisibilidad por ambos: Si el numero es divisible por 5, devolveras "Buzz" \n Divisibilidad por 3: Si el numero es divisible por ambos, devolveras "FizzBuzz \n No es divisible ni por 3 ni por 5: Si el número no es divisible ni por 3 ni por 5, devolverás el número en forma de cadena. \n Entrada: n: int : Un número entero. \n Salidas: str: devuelve "Fizz", "Buzz", "FizzBuzz", o el numero en forma de cadena ',
            'image_url': url_for('static', filename='img/fizzbuzz-logo.png'),
            'stars': 5,
            'test': {
                'one': {'description': 'Prueba #1', 'result': True},
                'two': {'description': 'Prueba #2', 'result': False},
                'three': {'description': 'Prueba #3', 'result': True},
            },
            'languages': {
                'python': {'code': 'def fizzbuzz(numbers):\n    result = []\n    for number in numbers:\n        if number % 3 == 0 and number % 5 == 0:\n            result.append("FizzBuzz")\n        elif number % 3 == 0:\n            result.append("Fizz")\n        elif number % 5 == 0:\n            result.append("Buzz")\n        else:\n            result.append(number)\n    return result'},
                'c#': {'code': '/* C code */\n#include <stdio.h>\nvoid fizzbuzz(int numbers[], int length) {\n    for (int i = 0; i < length; i++) {\n        if (numbers[i] % 3 == 0 && numbers[i] % 5 == 0) printf("FizzBuzz\\n");\n        else if (numbers[i] % 3 == 0) printf("Fizz\\n");\n        else if (numbers[i] % 5 == 0) printf("Buzz\\n");\n        else printf("%d\\n", numbers[i]);\n    }\n}'}
            }
        },            
        {
            'title': 'Palindrome',
            'problem': 'Verificar si una palabra es palíndromo, un palíndromo es una palabra que se lee igual al derecho y al revez, ignorando espacios \n Entrada: word: str \n Salidas: bool : True Si la palabra es palindromo, False en caso contrario',
            'image_url': url_for('static', filename='img/buble-logo.png'),
            'stars': 3,
            'test': {
                'one': {'description': 'Prueba #1', 'result': True},
                'two': {'description': 'Prueba #2', 'result': False},
                'three': {'description': 'Prueba #3', 'result': True},
            },
            'languages': {
                'python': {'code': 'def fizzbuzz(numbers):\n    result = []\n    for number in numbers:\n        if number % 3 == 0 and number % 5 == 0:\n            result.append("FizzBuzz")\n        elif number % 3 == 0:\n            result.append("Fizz")\n        elif number % 5 == 0:\n            result.append("Buzz")\n        else:\n            result.append(number)\n    return result'},
                'c#': {'code': '/* C code */\n#include <stdio.h>\nvoid fizzbuzz(int numbers[], int length) {\n    for (int i = 0; i < length; i++) {\n        if (numbers[i] % 3 == 0 && numbers[i] % 5 == 0) printf("FizzBuzz\\n");\n        else if (numbers[i] % 3 == 0) printf("Fizz\\n");\n        else if (numbers[i] % 5 == 0) printf("Buzz\\n");\n        else printf("%d\\n", numbers[i]);\n    }\n}'}
            }
        },
        {
            'title': 'BinarySearch',
            'problem': 'Realiza una busqueda binario en un arreglo ordenado para encontrar la posicion de un valor objetivo \n Entrada: arr (Un arreglo ordenado de elementos), target(El valor que se desea encontrar \n Salida: int: El indice del target en el arreglo si se encuentra, Si no es en el arreglo se devuelve -1) ',
            'image_url': url_for('static', filename='img/binary-logo.png'),
            'stars': 4,
            'test': {
                'one': {'description': 'Prueba #1', 'result': False},
                'two': {'description': 'Prueba #2', 'result': False},
                'three': {'description': 'Prueba #3', 'result': False},
                'Four': {'description': 'Prueba #4', 'result': False},
                'Five': {'description': 'Prueba #5', 'result': False},
            },
            'languages': {
                'python': {'code': 'def fizzbuzz(numbers):\n    result = []\n    for number in numbers:\n        if number % 3 == 0 and number % 5 == 0:\n            result.append("FizzBuzz")\n        elif number % 3 == 0:\n            result.append("Fizz")\n        elif number % 5 == 0:\n            result.append("Buzz")\n        else:\n            result.append(number)\n    return result'},
                'c#': {'code': '/* C code */\n#include <stdio.h>\nvoid fizzbuzz(int numbers[], int length) {\n    for (int i = 0; i < length; i++) {\n        if (numbers[i] % 3 == 0 && numbers[i] % 5 == 0) printf("FizzBuzz\\n");\n        else if (numbers[i] % 3 == 0) printf("Fizz\\n");\n        else if (numbers[i] % 5 == 0) printf("Buzz\\n");\n        else printf("%d\\n", numbers[i]);\n    }\n}'}
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

