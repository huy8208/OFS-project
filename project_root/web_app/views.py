from django.shortcuts import render
from .models import Product

def index(request):
    """Placeholder index view"""
    return render(request, 'index.html')

def testing(request):
    print('output here: ')
    print(request.POST['COCONUT'])
    return render(request,'testing.html')