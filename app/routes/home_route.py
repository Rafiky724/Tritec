from flask import Blueprint, render_template, url_for

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def home():
    return render_template('index.html', title='FizzBuzz', description='El problema de FizzBuzz consiste en reemplazar los números de una lista con "Fizz" si son múltiplos de 3, "Buzz" si son múltiplos de 5, y "FizzBuzz" si son múltiplos de ambos.', image_url=url_for('static', filename='img/fizzbuzz-logo.png'), stars=5 )

