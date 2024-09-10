from flask import Blueprint, render_template

problem_bp = Blueprint('problem_bp', __name__)

@problem_bp.route('/problems')
def problems():
    problems = [
        {
            'title': 'FizzBuzz',
            'star': 1,
            'test': 2,
            'description': 'oli'
         },
    ]
    
    return render_template('problems.html', problems=problems)