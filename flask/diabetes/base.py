from flask import Flask
import pickle
import numpy as np
import sklearn

#loada the predicted model and the user
model=pickle.load(open('diabetes_model.pkl','rb'))

from flask import Flask, render_template,request

app = Flask(__name__)




# Route for the home page
@app.route('/')
def home():
    return render_template('diabetes.html',prediction_text='')  # Renders the about.html file

@app.route('/predict',methods=['POST'])
def predict():
    #retrieve the input fields from the from
    Pregnancies=float(request.form['Pregnancies'])
    Glucose=float(request.form['Glucose'])
    BloodPressure=float(request.form['BloodPressure'])
    SkinThickness=float(request.form['SkinThickness'])
    Insulin=float(request.form['Insulin'])
    BMI=float(request.form['BMI'])
    DiabetesPedigreeFunction=float(request.form['DiabetesPedigreeFunction'])
    Age=float(request.form['Age'])
    

    #prepare the inut data for the prediction
    input_data=np.array([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])


    #make the prediction
    prediction=model.predict(input_data)

    #get the predicted_class

    prediction_text=f"predict diabtese :{prediction[0]}"
    return render_template('diabetes.html',prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
