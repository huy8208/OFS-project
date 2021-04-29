from django.shortcuts import render, redirect

#Create your views here
from .models import *
from .forms import CreateCustomerRegistrationForm    # Django's built-in user form
from django.contrib import messages  # To add message whether login/registration sucesses or fails.
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# json stuff (checkout)
from django.http import JsonResponse
import json

# @login_required(login_url='login') User this when create payment/checkout
def index(request):
    """Placeholder index view"""
    randomProductsList = Product.objects.order_by('?')
    return render(request, 'index.html',context={'randomProductsList':randomProductsList})

def Meat_Seafood(request):
    """Placeholder Meat_Seafood view"""
    return render(request, 'Meat_and_Seafood.html')

def Fruits_Vegetables(request):
    """Placeholder Fruits_Vegetables view"""
    return render(request, 'Fruits_and_Vegetables.html')

def Pantry(request):
    """Placeholder Pantry view"""
    return render(request, 'Pantry.html')

def Beverages(request):
    """Placeholder Beverages view"""
    return render(request, 'Beverages.html')

def Dairy_Eggs(request):
    """Placeholder Dairy_Eggs view"""
    return render(request, 'Dairy_Eggs.html')

def Frozen_Foods(request):
    """Placeholder Frozen_Foods view"""
    return render(request, 'Frozen_Foods.html')

# Product Info Stuff
def RibeyePP(request):
    """Placeholder Ribeye Product Page view"""
    return render(request, 'ProductPages/RibeyePP.html')

def NewyorkPP(request):
    """Placeholder Newyork Product Page view"""
    return render(request, 'ProductPages/NewyorkPP.html')

def ChickenthighsPP(request):
    """Placeholder ChickenthighsPP Product Page view"""
    return render(request, 'ProductPages/ChickenthighsPP.html')

def Chickenbreasts(request):
    """Placeholder Chickenbreasts Product Page view"""
    return render(request, 'ProductPages/Chickenbreasts.html')

def Porkchops(request):
    """Placeholder Porkshops Product Page view"""
    return render(request, 'ProductPages/Porkchops.html')

def Bacon(request):
    """Placeholder Bacon Product Page view"""
    return render(request, 'ProductPages/Bacon.html')

def Shrimps(request):
    """Placeholder Shrimps Product Page view"""
    return render(request, 'ProductPages/Shrimps.html')

def Clam(request):
    """Placeholder Clam Product Page view"""
    return render(request, 'ProductPages/Clam.html')

def CheddarCheese(request):
    """Placeholder Cheddar Cheese Product Page view"""
    return render(request, 'ProductPages/CheddarCheese.html')

def LowFatMilk(request):
    """Placeholder Low Fat Milk Product Page view"""
    return render(request, 'ProductPages/LowFatMilk.html')

def WholeMilk(request):
    """Placeholder Whole Milk Product Page view"""
    return render(request, 'ProductPages/WholeMilk.html')

def CreamCheese(request):
    """Placeholder Cream Cheese Product Page view"""
    return render(request, 'ProductPages/CreamCheese.html')

def PlainYogurt(request):
    """Placeholder Plain Yogurt Product Page view"""
    return render(request, 'ProductPages/PlainYogurt.html')

def DozenEggs(request):
    """Placeholder Dozen Eggs Product Page view"""
    return render(request, 'ProductPages/DozenEggs.html')

def EggWhites(request):
    """Placeholder Egg Whites Product Page view"""
    return render(request, 'ProductPages/EggWhites.html')

def AmericanCheese(request):
    """Placeholder Egg Whites Product Page view"""
    return render(request, 'ProductPages/AmericanCheese.html')

def Banana(request):
    """Placeholder Banana Product Page view"""
    return render(request, 'ProductPages/Banana.html')

def Watermelon(request):
    """Placeholder Watermelon Product Page view"""
    return render(request, 'ProductPages/Watermelon.html')

def Mango(request):
    """Placeholder Mango Product Page view"""
    return render(request, 'ProductPages/Mango.html')

def Apple(request):
    """Placeholder apple Product Page view"""
    context = {'allProducts':Product.objects.first()}
    return render(request, 'ProductPages/Apple.html',context)

def Guava(request):
    """Placeholder guava Product Page view"""
    return render(request, 'ProductPages/Guava.html')

def Grapes(request):
    """Placeholder grapes Product Page view"""
    return render(request, 'ProductPages/Grapes.html')

def Orange(request):
    """Placeholder orange Product Page view"""
    return render(request, 'ProductPages/Orange.html')

def Lemon(request):
    """Placeholder lemon Product Page view"""
    return render(request, 'ProductPages/Lemon.html')

def Broccoli(request):
    """Placeholder broccoli Product Page view"""
    return render(request, 'ProductPages/Broccoli.html')

def Lettuce(request):
    """Placeholder Lettuce Product Page view"""
    return render(request, 'ProductPages/Lettuce.html')

def Carrots(request):
    """Placeholder carrots Product Page view"""
    return render(request, 'ProductPages/Carrots.html')

def Potato(request):
    """Placeholder potato Product Page view"""
    return render(request, 'ProductPages/Potato.html')

def Cucumber(request):
    """Placeholder cucumber Product Page view"""
    return render(request, 'ProductPages/Cucumber.html')

def Tomato(request):
    """Placeholder tomato Product Page view"""
    return render(request, 'ProductPages/Tomato.html')

def Garlic(request):
    """Placeholder garlic Product Page view"""
    return render(request, 'ProductPages/Garlic.html')

def Onion(request):
    """Placeholder onion Product Page view"""
    return render(request, 'ProductPages/Onion.html')

def SourdoughBread(request):
    """Placeholder onion Product Page view"""
    return render(request, 'ProductPages/SourdoughBread.html')

def PeanutButter(request):
    """Placeholder onion Product Page view"""
    return render(request, 'ProductPages/PeanutButter.html')

def Pickles(request):
    """Placeholder onion Product Page view"""
    return render(request, 'ProductPages/Pickles.html')

def Sugar(request):
    """Placeholder onion Product Page view"""
    return render(request, 'ProductPages/Sugar.html')

def Cheerios(request):
    """Placeholder onion Product Page view"""
    return render(request, 'ProductPages/Cheerios.html')

def BrownRice(request):
    """Placeholder onion Product Page view"""
    return render(request, 'ProductPages/BrownRice.html')

def CannedBeans(request):
    """Placeholder onion Product Page view"""
    return render(request, 'ProductPages/CannedBeans.html')

def Oreos(request):
    """Placeholder onion Product Page view"""
    return render(request, 'ProductPages/Oreos.html')


def registration_page(request):
    """ This function does 3 tasks:
        1. Display register.html path.
        2. Using a default form from forms.py, retrieve user's input from register.html page.
        3. Check if user's input is valid and if so, redirect to login page. """
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = CreateCustomerRegistrationForm()
        if request.method == 'POST':
            form = CreateCustomerRegistrationForm(request.POST) # Pass in user's information from registration.login
            if form.is_valid():
                form.save()  # Create new user in admin/
                user_email = form.cleaned_data.get('email')
                messages.success(request,'Account was created for ' + user_email)
                return redirect('login')
        context = {'registration_form':form}
        return render(request, 'accounts/register.html',context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request,username=email,password=password)
            if user is not None:
                login(request,user)
                return redirect('homepage')
            else:
                messages.info(request,'Email or password is incorrect!')
        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def SearchPage(request):
    srh = request.GET['query']
    products = product.objects.filter(name__icontains=srh)
    params = {'products': products, 'search':srh}
    return render(request, 'SearchPage.html', params)

def cart_page(request):
    """Return a list of ordered items"""
    if request.user.is_authenticated:
        customer = request.user
        #get_or_create get the customer fromt the db, if the customer is anynomous, we create a temporary anynomous customer.
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = OrderedItem.objects.all() #Get all ordered items object that an authenticated user has placed from our db.
    else: #If user is not authenticated/login
        items = [] #create an empty list of items.
        order = {'get_cart_total':0,'get_cart_items':0}

    context = {'items':items,'order':order}
    return render(request, 'cart.html', context)

def checkout_page(request):
    # context = {}
    # return render(request, 'checkout.html', context)
    # searchquery = request.GET['query']
    # products = Product.objects.filter(name__icontains=searchquery)
    # params = {'products': products, 'search':searchquery}
    # return render(request, 'SearchPage.html', params)
    if request.user.is_authenticated:
        customer = request.user
        #get_or_create get the customer fromt the db, if the customer is anynomous, we create a temporary anynomous customer.
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = OrderedItem.objects.all() #Get all ordered items object that an authenticated user has placed from our db.
    else: #If user is not authenticated/login
        items = [] #create an empty list of items.
        order = {'get_cart_total':0,'get_cart_items':0}

    context = {'items':items,'order':order}
    return render(request, 'checkout.html', context)

def processOrder(request):
    return JsonResponse("Payment complete!", safe = False)

def base_product_template(request):
    context = {'allProducts':Product.objects.first()}
    return render(request, 'ProductPages/base_product_template.html',context)

def product_detail(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'Product_detail.html',context={'product':product})

def updateItem(request):
    return JsonResponse('Item was added',safe = False)