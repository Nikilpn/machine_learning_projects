
from flask import Flask
from flask import render_template,request
import pickle
import numpy as np
import pandas as pd


#loaded the predicted model and the user
model=pickle.load(open('iris_model.pkl','rb'))

app=Flask(__name__)

#Route for the homepage
@app.route('/')
def home():
    return render_template('iris.html',prediction_text='')

@app.route('/predict',methods=['POST'])
def predict():
    sepal_length=float(request.form['sepal_length'])
    sepal_width=float(request.form['sepal_width'])
    petal_length=float(request.form['petal_length'])
    petal_width=float(request.form['petal_width'])

    #input data for the prediction
    input_data=np.array([[sepal_length,sepal_width,petal_length,petal_width]])

    #make the prediction
    prediction=model.predict(input_data)

    
    #get the predicted_class

    prediction_text=f"predict iris :{prediction[0]}"
    return render_template('iris.html',prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
