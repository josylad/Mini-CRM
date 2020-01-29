from django.conf import settings
from django.templatetags.static import static
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import *
from .forms import RegisterForm



# Create your views here.
def index(request):
    date = dt.date.today()
    companies = Companies.get_allcompany()
    
    return render(request, 'index.html', {"date": date, "companies":companies})


def employee(request):
    employees = Employee.get_allemployee()
    
    return render(request, 'employee.html', {"employees":employees})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            receiver=form.cleaned_data['email']
            
            return redirect('/')
        
    else:
        form = RegisterForm()
    return render(request, 'registration/registration_form.html', {'form':form})
    