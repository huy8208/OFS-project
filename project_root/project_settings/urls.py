"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name = "homepage"),
    # This is for the Departments tab on the left
    path('Meat_Seafood/', views.Meat_Seafood, name = "Meat_Seafood"),
    path('Fruits_Vegetables/', views.Fruits_Vegetables, name = "Fruits_Vegetables"),
    path('Pantry/', views.Pantry, name = "Pantry"),
    path('Beverages/', views.Beverages, name = "Beverages"),
    path('Dairy_Eggs/', views.Dairy_Eggs, name = "Dairy_Eggs"),
    path('Frozen_Foods/', views.Frozen_Foods, name = "Frozen_Foods"),
    # User registration and login
    path('login/',views.login_page,name = "login"),
    path('register/',views.registration_page,name = "register"),
    path('logout/',views.logoutUser,name = "logout")
    # Search Pages
    #path('search/', views.SearchPage, name='search_result'),
    # Cart and Checkout
    , path('cart/', views.cart_page, name = "cart")
    , path('checkout/', views.checkout_page, name = "checkout"),
    # individual Product Pages
    path('RibeyePP/', views.RibeyePP, name = "RibeyePP"),
    path('Newyork/', views.NewyorkPP, name = "NewyorkPP"),
    path('product_page_template/', views.base_product_template, name = "productBaseTemplate"),

]


