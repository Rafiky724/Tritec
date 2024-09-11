from flask import Blueprint, render_template, request, url_for

problem_bp = Blueprint('problem_bp', __name__)

@problem_bp.route('/problems')
def problems():
    
    value = request.args.get('value', default=None, type=int)
    
    problems = [
        {},
        {
            'title': 'FizzBuzz',
            'problem': 'Para realizar el algoritmo de FizzBuzz, primero debes tener una lista de números como entrada. Luego, recorres cada número de la lista uno a uno. Para cada número, revisas si es divisible por 3. Si es divisible por 3, reemplazas ese número con "Fizz". Si no es divisible por 3, pero es divisible por 5, reemplazas el número con "Buzz". Si el número es divisible tanto por 3 como por 5, entonces lo reemplazas con "FizzBuzz". Si el número no cumple con ninguna de estas condiciones, simplemente mantienes el número original en la lista. Al final del proceso, obtendrás una lista transformada donde cada número ha sido reemplazado de acuerdo con estas reglas.\n\nEsto es solo un texto guía. Ya luego tenemos que ser más claro en lo que tenemos que decir, lo que se tiene que tener en cuenta a la hora de realizar el código.',
            'image_url': url_for('static', filename='img/fizzbuzz-logo.png'),
            'stars': 5,
            'test': {
                'one': {'description': 'Prueba #1', 'result': True},
                'two': {'description': 'Prueba #2', 'result': False},
                'three': {'description': 'Prueba #3', 'result': True},
            }
        },
        {
            'title': 'BubbleSort',
            'problem': 'adios',
            'image_url': url_for('static', filename='img/buble-logo.png'),
            'stars': 3,
            'test': {
                'one': {'description': 'Prueba #1', 'result': True},
                'two': {'description': 'Prueba #2', 'result': False},
                'three': {'description': 'Prueba #3', 'result': True},
            }
        },
        {
            'title': 'BinarySearch',
            'problem': 'adios',
            'image_url': url_for('static', filename='img/binary-logo.png'),
            'stars': 4,
            'test': {
                'one': {'description': 'Prueba #1', 'result': True},
                'two': {'description': 'Prueba #2', 'result': False},
                'three': {'description': 'Prueba #3', 'result': True},
            },
        },
    ]
    
    for problem in problems:
        if 'problem' in problem:
            problem['problem'] = problem['problem'].replace('\n', '<br>')
    
    problem = problems[value] if value is not None and 0 <= value < len(problems) else None
    
    return render_template('problems.html', problem=problem)
