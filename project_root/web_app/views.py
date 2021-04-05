from django.shortcuts import render
from .models import Product,Customer

def index(request):
    """Placeholder index view"""
    return render(request, 'index.html')

def getCustomerInfo(request):
    print(request.POST)
    customer1 = Customer()
    customer1.firstName = request.POST['COCONUT']
    customer1.save()
    return render(request, 'testing.html')
