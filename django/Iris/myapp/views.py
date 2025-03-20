from django.shortcuts import render,redirect
from myapp.models import IrisDb
from .models import *
import pickle
import sklearn

# Create your views here.
def model_prediction(a,b,x,y):
    with open("./myapp/iris_model.pkl", "rb") as file:
        model = pickle.load(file)
        predict = model.predict([[a, b, x, y]]) 
        return predict



def home_page(req):
    return render(req,"index.html")

def save_page(request):
    if request.method=="POST":
        sl=float(request.POST.get('sepal_length'))
        sw=float(request.POST.get('sepal_width'))
        p_l=float(request.POST.get('petal_length'))
        p_w=float(request.POST.get('petal_width'))
        obj=IrisDb(sepal_length=sl,sepal_width=sw,petal_length=p_l,petal_width=p_w)
        obj.save()
        pred = model_prediction(sl,sw,p_l,p_w)
        print(f"{pred}")
        return render(request, 'index.html', {'prediction': pred})

