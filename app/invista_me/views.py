from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
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