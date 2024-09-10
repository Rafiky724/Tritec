from flask import Blueprint, render_template

problem_bp = Blueprint('problem_bp', __name__)

@problem_bp.route('/problemas')
def problems():
    return render_template('problems.html')