import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__, template_folder= 'template') #create flask app
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/predict',methods = ['POST']) #model will provide output for inputs

def predict():


    int_features = [float(x) for x in request.form.values()]
    features = [np.array(int_features)]
    prediction = model.predict(features)

    output = prediction[0]

    return render_template('pred.html', prediction_text = 'Survival Predection: {}'.format(output))

if __name__== "__main__":
    app.run(debug= True)
