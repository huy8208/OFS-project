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
from django.conf.urls.static import static
from django.conf import settings

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
    path('logout/',views.logoutUser,name = "logout"),
    # Search Pages
    #path('search/', views.SearchPage, name='search_result'),
    path('search/', views.SearchPage, name='search_result'),
    # Cart and Checkout
    path('cart/', views.cart_page, name = "cart"),
    path('profile/', views.profile_page, name = "profile"),
    path('update_item/', views.updateItem, name = "update_item"),
    path('checkout/', views.checkout_page, name = "checkout"),
    #Dynamic product pages
    path('product_detail/<str:pk>',views.product_detail,name='product_detail'),
    #Base template
    path('base_template/', views.base_template, name = "base_template"),
    #Payment
    path('success/', views.success, name = "success"),
    path('cancel/', views.cancel, name = "cancel"),
    path('create-checkout-session/',views.CreateCheckoutSessionView.as_view(),name='create-checkout-session'),
    path('webhook/',views.stripe_webhook,name='webhook'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
