from django.shortcuts import render, redirect

#Create your views here
from .models import *
from .forms import CreateCustomerRegistrationForm  # Django's built-in user form
from django.contrib import messages  # To add message whether login/registration sucesses or fails.
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


from django.http import JsonResponse
import json
#Stripe
from django.views import View
import stripe
from project_settings import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

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
    # yes = OrderedItem.objects.select_related()
    

    context = {'items':items,'order':order,'STRIPE_PUBLIC_KEY':settings.STRIPE_PUBLIC_KEY,'STRIPE_URL':settings.STRIPE_URL}
    return render(request, 'payment/cart.html', context)

def profile_page(request):
    if request.user.is_authenticated:
        customer = request.user
        #get_or_create get the customer fromt the db, if the customer is anynomous, we create a temporary anynomous customer.
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = OrderedItem.objects.all() #Get all ordered items object that an authenticated user has placed from our db.
    else: #If user is not authenticated/login
        items = [] #create an empty list of items.
        order = {'get_cart_total':0,'get_cart_items':0}

    context = {'items':items,'order':order}
    return render(request, 'accounts/profile.html', context)

def processOrder(request):
    return JsonResponse("Payment complete!", safe = False)


def product_detail(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'Product_detail.html',context={'product':product})

def updateItem(request):
    """Update user's orderedItem in db"""
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:',action)
    print('Product:',productId)

    customer = request.user
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,created = OrderedItem.objects.get_or_create(order=order,product=product)

    """If orderItem is exceeded amount_in_stock => stop here"""


    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added',safe = False)

def base_template(request):
    if request.user.is_authenticated:
        customer = request.user
        #get_or_create get the customer fromt the db, if the customer is anynomous, we create a temporary anynomous customer.
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = OrderedItem.objects.all() #Get all ordered items object that an authenticated user has placed from our db.
        cartItems = order.get_cart_items
    else: #If user is not authenticated/login
        items = [] #create an empty list of items.
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
    context = {'cartItems':cartItems}
    return render(request,'base_template.html',context=context)

def success(request):
    return render(request,'payment/success.html')

def cancel(request):
    return render(request,'payment/cancel.html')

#Class view
class CreateCheckoutSessionView(View):
    def post(self,request,*args,**kwargs):
        print(json.loads(request.body)['lineItems'])
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            shipping_rates= ["shr_1ImByjBew4cXzmng8ppGn2s5"],
            shipping_address_collection={'allowed_countries': ['US', 'CA'],},
            line_items=json.loads(request.body)['lineItems'],
            mode='payment',
            success_url=settings.STRIPE_URL + '/success/',
            cancel_url=settings.STRIPE_URL + '/cancel/',
        )
        return JsonResponse({'id':checkout_session.id})
        # return JsonResponse(json.loads(request.body)['lineItems'])

