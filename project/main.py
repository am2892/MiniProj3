from flask import Blueprint, render_template, request
from . import db
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

logCount = []

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():

    if request.method == 'POST':
        dataset = request.form['dataset']
        operation = request.form['function']

        if operation == 'mean':
            logCount.append('mean of ' + dataset)
            from project.StatisticalFunctions import populationMean
            answer = float(populationMean(dataset))
            return render_template('profile.html', answer=answer, logCount=logCount, name=current_user.name)
        elif operation == 'median':
            logCount.append('median of ' + dataset)
            from project.StatisticalFunctions import median
            answer = float(median(dataset))
            return render_template('profile.html', answer=answer, logCount=logCount, name=current_user.name)
        elif operation == 'mode':
            logCount.append('mode of ' + dataset)
            from project.StatisticalFunctions import mode
            answer = float(mode(dataset))
            return render_template('profile.html', answer=answer, logCount=logCount, name=current_user.name)
        elif operation == 'variance':
            logCount.append('variance of ' + dataset)
            from project.StatisticalFunctions import variance
            answer = float(variance(dataset))
            return render_template('profile.html', answer=answer, logCount=logCount, name=current_user.name)
        else:
            return render_template('profile.html', name=current_user.name)
    

    return render_template('profile.html', name=current_user.name)
