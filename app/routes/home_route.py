from flask import Blueprint, render_template, url_for

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
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
            'title': 'BubleSort',
            'description': 'El algoritmo de Bubble Sort ordena una lista comparando y, si es necesario, intercambiando pares de elementos adyacentes. Repite el proceso hasta que toda la lista esté ordenada.',
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
