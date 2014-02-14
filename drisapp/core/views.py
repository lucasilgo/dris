from django.shortcuts import render
from drisapp.core.forms import CalculateForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def calculate(request):
    return render(request, 'calculate.html', {'form': CalculateForm()})

def converte_norma(norma):
    return [float(x) for x in a.split(', ')]