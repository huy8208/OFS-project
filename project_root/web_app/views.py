from django.shortcuts import render
from .models import Product,Customer

def index(request):
    """Placeholder index view"""
    return render(request, 'index.html')

def Meat_Seafood(request):
    """Placeholder index view"""
    return render(request, 'Meat_and_Seafood.html')

def Fruits_Vegetables(request):
    """Placeholder index view"""
    return render(request, 'Fruits_and_Vegetables.html')

def Pantry(request):
    """Placeholder index view"""
    return render(request, 'Pantry.html')

def Beverages(request):
    """Placeholder index view"""
    return render(request, 'Beverages.html')

def Dairy_Eggs(request):
    """Placeholder index view"""
    return render(request, 'Dairy_Eggs.html')

def Frozen_Foods(request):
    """Placeholder index view"""
    return render(request, 'Frozen_Foods.html')

def getCustomerInfo(request):
    print(request.POST)
    customer1 = Customer()
    customer1.firstName = request.POST['COCONUT']
    customer1.save()
    return render(request, 'testing.html')
