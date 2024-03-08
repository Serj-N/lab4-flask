from flask import Flask, render_template, request

app = Flask('lab4')


@app.route('/')
def show_start_form():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    form = request.form
    if request.method == 'POST':
        number = request.form['number']
        fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
        predict = fib(int(number))
    return render_template('resultsform.html', number=number, predicted_number=predict)


app.run()
