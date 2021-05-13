#Create your views here
from django.shortcuts import render, redirect
from .models import *
# Django's built-in user form
from .forms import CreateCustomerRegistrationForm, CreateShippingAddressForm
# To add message whether login/registration sucesses or fails.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from project_settings import settings
import os
import smtplib
import imghdr

#Http response
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
import json
#Stripe
from django.views import View
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
endpoint_secret = 'whsec_RXRtRwQFV2iW8XyUfTCThW4wG5DWUb30'

# @login_required(login_url='login') User this when create payment/checkout
def index(request):
    """Placeholder index view"""
    showlist = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user
        #get_or_create get the customer fromt the db, if the customer is anynomous, we create a temporary anynomous customer.
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        # Get all ordered items object that an authenticated user has placed from our db.
        cartItems = order.get_cart_items
    else:  # If user is not authenticated/login
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        # To update the quantity icon at the top right.
        cartItems = order['get_cart_items']
    randomProductsList = Product.objects.order_by('?')
    return render(request, 'index.html', context={'randomProductsList': randomProductsList,'cartItems': cartItems,'order': order,'showlist':showlist})


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
            # Pass in user's information from registration.login
            form = CreateCustomerRegistrationForm(request.POST)
            if form.is_valid():
                form.save()  # Create new user in admin/
                user_email = form.cleaned_data.get('email')
                messages.success(
                    request, 'Account was created for ' + user_email)
                return redirect('login')
        context = {'registration_form': form}
        return render(request, 'accounts/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, 'Email or password is incorrect!')
        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def SearchPage(request):
    srh = request.GET['query']
    allProducts = Product.objects.all()
    products = Product.objects.filter(name__icontains=srh)
    params = {'products': products, 'search': srh,'allProducts':allProducts}

    if len(products) != 1: #If the product does not exist or search wasn't specific enoug
        return render(request, 'redirect.html')

    return render(request, 'SearchPage.html', params)
    

def cart_page(request):
    """Return a list of ordered items"""
    if request.user.is_authenticated:
        customer = request.user
        #get_or_create get the customer fromt the db, if the customer is anynomous, we create a temporary anynomous customer.
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        # Get all ordered items object that an authenticated user has placed from our db.
        items = order.items_in_cart.all()
        cartItems = order.get_cart_items
    else:  # If user is not authenticated/login
        items = []  # create an empty list of items.
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    
    context = {'items': items, 'order': order,'cartItems': cartItems, 'STRIPE_PUBLIC_KEY':
               settings.STRIPE_PUBLIC_KEY, 'STRIPE_URL': settings.STRIPE_URL}
    return render(request, 'payment/cart.html', context)


@login_required(login_url='login')
def checkout_page(request):
    customer = request.user  # Need to restructure if we wanna do anonymous login
    if request.user.is_authenticated:
        #get_or_create get the customer fromt the db, if the customer is anynomous, we create a temporary anynomous customer.
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        # Get all ordered items object that an authenticated user has placed from our db.
        items = order.items_in_cart.all()
        cartItems = order.get_cart_items
    else:  # If user is not authenticated/login
        items = []  # create an empty list of items.
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {'customer': customer, 'items': items, 'order': order,'cartItems': cartItems,
               'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY, 'STRIPE_URL': settings.STRIPE_URL}
    return render(request, 'payment/checkout.html', context)


def create_stripe_order(request):
    """This method creates a new stripe order using stripe api.
    Unable to create stripe order without skus."""
    customer = request.user
    if request.method == 'POST':
        jsonObject = json.loads(request.body)
        json_formatted_str = json.dumps(jsonObject, indent=2)
        print(json_formatted_str)
        shippingAddress = json.loads(request.body)[
            'shippingInfo']['customer_info']
        stripe.Order.create(
            currency="usd",
            email=customer.email,
            shipping={
                "name": shippingAddress['firstname']+" "+shippingAddress['lastname'],
                "address": {
                    "line1": shippingAddress['address'],
                    "city": shippingAddress['city'],
                    "state": shippingAddress['state'],
                    "country": shippingAddress['country'],
                    "postal_code": shippingAddress['zipcode'],
                },
            },
        )
        return HttpResponse(status=200)
    else:
        print("create_order def unidentified error!")
        return HttpResponse(status=500)


@login_required(login_url='login')
def profile_page(request):
    customer = request.user
    context = {"customer": customer}
    return render(request, 'accounts/profile.html', context)


def save_user_info(request):
    customer = request.user
    if request.method == 'POST':
        customerAddressForm = json.loads(request.body)['userFormData']
        shippingObject, created = ShippingAddress.objects.get_or_create(
            customer=customer)
        shippingObject.first_name = customerAddressForm['firstname']
        shippingObject.last_name = customerAddressForm['lastname']
        shippingObject.address = customerAddressForm['address']
        shippingObject.city = customerAddressForm['city']
        shippingObject.state = customerAddressForm['state']
        shippingObject.zipcode = customerAddressForm['zipcode']
        shippingObject.country = customerAddressForm['country']
        shippingObject.phone = customerAddressForm['phone']
        shippingObject.save()
        return JsonResponse({'customer_info': customerAddressForm})
    else:
        return HttpResponse(status=500)


def processOrder(request):
    return JsonResponse("Payment complete!", safe=False)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'Product_detail.html', context={'product': product})


def updateItem(request):
    """Update user's orderedItem in db"""
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    # print('Action:', action)
    # print('Product:', productId)

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderedItem.objects.get_or_create(
        order=order, product=product)

    """If orderItem is exceeded amount_in_stock => stop here"""
    # if(self.product.amount_in_stock < self.quantity || self.product.amount_in_stock == 0):
    #     return False
    # else:
    #     return True
    if action == 'add':
        if product.amount_in_stock <= orderItem.quantity:
            messages.error(request, 'Not enough stock.')
        else:
            orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def update_cart_based_on_quantity(request):
    print("rewoqjnroeiwjqroqwejtorehjtuwerh")
    customer = request.user
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        userQuantity = int(data['user_quantity'])
        action = data['action']
        productId = int(data['product_id'])
        print("userQuantity",userQuantity)
        print("action",action)
        print("productId",productId)
        customer = request.user
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        orderItem, created = OrderedItem.objects.get_or_create(
            order=order, product=product)
        if action == 'add':
            print("Amount in stock:",product.amount_in_stock)
            print("Quantity:",orderItem.quantity)
            if product.amount_in_stock <= orderItem.quantity:
                messages.error(request, 'Not enough stock.')
            else:
                orderItem.quantity += userQuantity
        orderItem.save()
        return JsonResponse({"yeah":"Specific quantity was added"})
    else:
        return HttpResponse(status=500)

def deleteItemFromCart(request):
    pass


def base_template(request):
    if request.user.is_authenticated:
        customer = request.user
        #get_or_create get the customer fromt the db, if the customer is anynomous, we create a temporary anynomous customer.
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        # Get all ordered items object that an authenticated user has placed from our db.
        cartItems = order.get_cart_items
    else:  # If user is not authenticated/login
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        # To update the quantity icon at the top right.
        cartItems = order['get_cart_items']
    context = {'cartItems': cartItems,'order': order}
    return render(request, 'base_template.html', context=context)


def success(request):
    return render(request, 'payment/success.html')


def cancel(request):
    return render(request, 'payment/cancel.html')


#Class view
class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            customer_email=request.user.email,
            line_items=json.loads(request.body)['lineItems'],
            mode='payment',
            success_url=settings.STRIPE_URL + '/success/',
            cancel_url=settings.STRIPE_URL + '/cancel/',
        )
        return JsonResponse({'id': checkout_session.id})


def send_email_confirmation(session):
    # from email.mime.text import MIMEText
    from django.core.mail import send_mail
    from django.template.loader import render_to_string
    from django.utils.html import strip_tags

    subject = 'OFS Order Confirmation'
    html_message = render_to_string('email/email.html')
    plain_message = strip_tags(html_message)
    from_email = 'cmpeOFS@gmail.com'
    to = session['customer_email']
    
    send_mail(subject=subject,message=plain_message,from_email=from_email,recipient_list=[to],fail_silently=False,html_message=html_message)

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fulfill the purchase...
        fulfill_order(session)
    # Passed signature verification
    return HttpResponse(status=200)

def emptyCart(session):
    customer = Customer.objects.get(email=session['customer_email'])
    order, created = Order.objects.get_or_create(
    customer=customer, complete=False)
    order.items_in_cart.all().delete()
    
def fulfill_order(session):
    # TODO: fill me in
    # Saving a copy of the order in our own dabase.
    # approve_customer_order(session)
    # Sending customer a receipt email
    # send_email_confirmation(session)
    print("Fulfilling order", session)
    update_stock(session)
    #Empty customer's cart
    emptyCart(session)

def update_stock(session):
    # Update stock
    customer = Customer.objects.get(email=session['customer_email'])
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderedItem.objects.get_or_create(order=order)
    product = orderItem.product
    product.amount_in_stock =  product.amount_in_stock - orderItem.quantity
    product.save()

def approve_customer_order(session):
    customer = Customer.objects.get(email=session['customer_email'])
    #Get shippingAddress obj if it exists, else create new.
    order, created = Order.objects.get_or_create(customer=customer)
    order.status = order.STATUS[0]
    order.checkout = order.CHECKOUT[0]
    order.save()


# Commented out, probably not using it because adding
# address does not prefill stripe checkout
# class CreateCheckoutSessionView(View):
#     def post(self,request,*args,**kwargs):
#         address = {'city': 'San Jose', 'country': 'USA',
#         'line1': 'testing ct', 'line2': 'none',
#         'postal_code': '95138', 'state': 'CA'}
#         stripe_customer = stripe.Customer.create(address=address,shipping={"address":address,"name":request.user},email=request.user.email)

#         checkout_session = stripe.checkout.Session.create(
#             customer=stripe_customer,
#             payment_method_types=['card'],
#             shipping_rates= ["shr_1ImByjBew4cXzmng8ppGn2s5"],
#             shipping_address_collection={'allowed_countries': ['US', 'CA'],},
#             line_items=json.loads(request.body)['lineItems'],
#             mode='payment',
#             success_url=settings.STRIPE_URL + '/success/',
#             cancel_url=settings.STRIPE_URL + '/cancel/',
#         )
#         return JsonResponse({'id':checkout_session.id})
