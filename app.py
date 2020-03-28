from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')

logCount = []

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        dataset = request.form['dataset']
        operation = request.form['function']

        if operation == 'mean':
            logCount.append('mean of ' + dataset)
            from StatisticalFunctions import populationMean
            answer = float(populationMean(dataset))
            return render_template('app.html', answer=answer, logCount=logCount)
        elif operation == 'median':
            logCount.append('median of ' + dataset)
            from StatisticalFunctions import median
            answer = float(median(dataset))
            return render_template('app.html', answer=answer, logCount=logCount)
        elif operation == 'mode':
            logCount.append('mode of ' + dataset)
            from StatisticalFunctions import mode
            answer = float(mode(dataset))
            return render_template('app.html', answer=answer, logCount=logCount)
        elif operation == 'variance':
            logCount.append('variance of ' + dataset)
            from StatisticalFunctions import variance
            answer = float(variance(dataset))
            return render_template('app.html', answer=answer, logCount=logCount)
        else:
            return render_template('app.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()