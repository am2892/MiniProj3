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
        elif operation == 'variance-population':
            logCount.append('variance population proportion of ' + dataset)
            from project.StatisticalFunctions import variancePopulationProportion
            answer = float(variancePopulationProportion(dataset))
            return render_template('profile.html', answer=answer, logCount=logCount, name=current_user.name)
        elif operation == 'z-score':
            logCount.append('zScores of ' + dataset)
            from project.StatisticalFunctions import zScore
            answer = zScore(dataset)
            return render_template('profile.html', answer=answer, logCount=logCount, name=current_user.name)
        elif operation == 'standardized-score':
            logCount.append('standardized score of ' + dataset)
            from project.StatisticalFunctions import standardizedScore
            answer = standardizedScore(dataset)
            return render_template('profile.html', answer=answer, logCount=logCount, name=current_user.name)
        elif operation == 'ppc':
            logCount.append('population correlation coefficient of ' + dataset)
            from project.StatisticalFunctions import populationCorrelationCoefficient
            answer = float(populationCorrelationCoefficient(dataset))
            return render_template('profile.html', answer=answer, logCount=logCount, name=current_user.name)
        else:
            return render_template('profile.html', name=current_user.name)
    

    return render_template('profile.html', name=current_user.name)
