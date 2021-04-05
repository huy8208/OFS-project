from django.shortcuts import render
from .models import Product

def index(request):
    """Placeholder index view"""
    return render(request, 'index.html')

def testing(request):
    print('output here: ')
    print(request.POST['COCONUT'])
    product1 = Product()
    product1.productName = request.POST['COCONUT']
    print('printing product1: ',product1)
    product1.save()


    return render(request,'testing.html')
