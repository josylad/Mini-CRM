from django.conf import settings
from django.templatetags.static import static
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import *



# Create your views here.
def index(request):
    date = dt.date.today()
    companies = Companies.get_allcompany()
    
    return render(request, 'index.html', {"date": date, "companies":companies})

