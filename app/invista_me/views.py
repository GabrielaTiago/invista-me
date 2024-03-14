from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(_):
    return HttpResponse('Home Page!!')

def about(request):
    user = {
        'first_name': 'Gabriela',
        'last_name': 'Tiago',
        'email': 'gabriela@email.com',
        'age': 22,
        'job': 'Developer',
    }
    return render(request, 'hero/about.html', user)

# Investments views

def new_investment(request):
    return render(request, 'investments/new_investment.html')

def registered_investment(request):
    investment = {
        'name': request.POST.get('name'),
        'type': request.POST.get('type'),
        'value': request.POST.get('value')
    }
    return render(request, 'investments/registered_investment.html', investment)