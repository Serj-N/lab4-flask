import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask('lab4')
FILENAME = 'diabetes_model.sav'


@app.route('/')
def show_start_form():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    form = request.form
    if request.method == 'POST':
        x = request.form['number']
        value = np.array([float(x)])
        loaded_model = pickle.load(open(str(FILENAME), 'rb'))
        predicted_y = loaded_model.predict(value.reshape(1, -1))
        return render_template('resultsform.html', number=x, predicted_number=predicted_y[0][0])


app.run()
