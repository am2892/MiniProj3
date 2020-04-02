from flask import Blueprint, render_template, request
from . import db
from flask_login import login_required, current_user
from .models import functions

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

def returnCorrectHistory(history, itemsToReturn):
    for item in history:
        if item.userName == current_user.name:
            itemsToReturn.append(item)

def deleteCorrectItems(history, itemsToReturn):
    for item in history:
        if item.userName == current_user.name:
            db.session.delete(item)
            db.session.commit()
    itemsToReturn=history

@main.route('/delete_component/<component_id>')
@login_required
def delete_component(component_id):
    component = functions.query.filter_by(id=component_id).first_or_404()
    db.session.delete(component)
    db.session.commit() 
    itemsToReturn = []
    history = functions.query.all()
    for item in history:
        if item.userName == current_user.name:
            itemsToReturn.append(item)
    return render_template('profile.html', logCount=itemsToReturn, name=current_user.name)

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        dataset = request.form['dataset']
        operation = request.form['function']
        
        if operation == 'deleteAll':
            print('delete')
            # functions.query.delete()
            # db.session.commit()
            history = functions.query.all()
            itemsToReturn = []
            deleteCorrectItems(history, itemsToReturn)
            return render_template('profile.html', logCount=itemsToReturn, name=current_user.name)
        if operation == 'deleteOne':
            print('delete one')
        if operation == 'mean':
            new_function = functions(userName=current_user.name,functionName='mean', numbers=dataset)
            db.session.add(new_function)
            db.session.commit()
            history = functions.query.all()
            itemsToReturn = []
            returnCorrectHistory(history, itemsToReturn)
            from project.StatisticalFunctions import populationMean
            answer = float(populationMean(dataset))
            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name)
        elif operation == 'median':
            new_function = functions(userName=current_user.name,functionName='median',numbers=dataset)
            db.session.add(new_function)
            db.session.commit()
            history = functions.query.all()
            itemsToReturn = []
            returnCorrectHistory(history, itemsToReturn)
            from project.StatisticalFunctions import median
            answer = float(median(dataset))
            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name)
        elif operation == 'mode':
            new_function = functions(userName=current_user.name,functionName='mode', numbers=dataset)
            db.session.add(new_function)
            db.session.commit()
            history = functions.query.all()
            itemsToReturn = []
            returnCorrectHistory(history, itemsToReturn)
            from project.StatisticalFunctions import mode
            answer = float(mode(dataset))
            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name)
        elif operation == 'variance':
            new_function = functions(userName=current_user.name,functionName='variance', numbers=dataset)
            db.session.add(new_function)
            db.session.commit()
            history = functions.query.all()
            itemsToReturn = []
            returnCorrectHistory(history, itemsToReturn)
            from project.StatisticalFunctions import variance
            answer = float(variance(dataset))
            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name)
        elif operation == 'variance-population':
            new_function = functions(userName=current_user.name,functionName='variancePopulationProportion', numbers=dataset)
            db.session.add(new_function)
            db.session.commit()
            history = functions.query.all()
            itemsToReturn = []
            returnCorrectHistory(history, itemsToReturn)
            from project.StatisticalFunctions import variancePopulationProportion
            answer = float(variancePopulationProportion(dataset))
            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name)
        elif operation == 'z-score':
            new_function = functions(userName=current_user.name,functionName='zScore', numbers=dataset)
            db.session.add(new_function)
            db.session.commit()
            history = functions.query.all()
            itemsToReturn = []
            returnCorrectHistory(history, itemsToReturn)
            from project.StatisticalFunctions import zScore
            answer = zScore(dataset)
            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name)
        elif operation == 'standardized-score':
            new_function = functions(userName=current_user.name,functionName='standardizedScore', numbers=dataset)
            db.session.add(new_function)
            db.session.commit()
            history = functions.query.all()
            itemsToReturn = []
            returnCorrectHistory(history, itemsToReturn)
            from project.StatisticalFunctions import standardizedScore
            answer = standardizedScore(dataset)
            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name)
        elif operation == 'ppc':
            new_function = functions(userName=current_user.name,functionName='PPC', numbers=dataset)
            db.session.add(new_function)
            db.session.commit()
            history = functions.query.all()
            itemsToReturn = []
            returnCorrectHistory(history, itemsToReturn)
            from project.StatisticalFunctions import populationCorrelationCoefficient
            answer = float(populationCorrelationCoefficient(dataset))
            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name)
        else:
            return render_template('profile.html', name=current_user.name)
    
    history = functions.query.all()
    itemsToReturn = []
    returnCorrectHistory(history, itemsToReturn)
    return render_template('profile.html', name=current_user.name, logCount=itemsToReturn)
