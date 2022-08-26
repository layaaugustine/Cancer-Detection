from multiprocessing import context
from django.shortcuts import render,redirect
from .form import CancerForms
from .models import Cancer
# Create your views here.

def index(request):
    if request.method =='POST':
        form = CancerForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cancerapp-prediction")
    else:
        form = CancerForms()

    context = {
        'form':form
    }

    return render(request,'CancerApp/index.html',context)

def prediction(request):

    prediction_data = Cancer.objects.all()

    context={
        'prediction_data':prediction_data
    }
    return render(request,"CancerApp/prediction.html",context)