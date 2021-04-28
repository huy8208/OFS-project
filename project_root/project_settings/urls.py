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
    path('logout/',views.logoutUser,name = "logout")
    # Search Pages
    #path('search/', views.SearchPage, name='search_result'),
    # Cart and Checkout
    , path('cart/', views.cart_page, name = "cart")
    , path('checkout/', views.checkout_page, name = "checkout"),
    # individual Product Pages
    path('RibeyePP/', views.RibeyePP, name = "RibeyePP"),
    path('Newyork/', views.NewyorkPP, name = "NewyorkPP"),
    path('ChickenthighsPP/', views.ChickenthighsPP, name = "ChickenthighsPP"),
    path('Chickenbreasts/', views.Chickenbreasts, name = "Chickenbreasts"),
    path('Porkchops/', views.Porkchops, name = "Porkchops"),
    path('Bacon/', views.Bacon, name = "Bacon"),
    path('Shrimps/', views.Shrimps, name = "Shrimps"),
    path('Clam/', views.Clam, name = "Clam"),
    path('product_page_template/', views.base_product_template, name = "productBaseTemplate"),
    path('Cheddar/', views.CheddarCheese, name = "CheddarCheese"),
    path('LowFatMilk/', views.LowFatMilk, name = "LowFatMilk"),
    path('WholeMilk/', views.WholeMilk, name = "WholeMilk"),
    path('CreamCheese/', views.CreamCheese, name = "CreamCheese"),
    path('PlainYogurt/', views.PlainYogurt, name = "PlainYogurt"),
    path('DozenEggs/', views.DozenEggs, name = "DozenEggs"),
    path('EggWhites/', views.EggWhites, name = "EggWhites"),
    path('AmericanCheese/', views.AmericanCheese, name = "AmericanCheese"),
    path('Mango/', views.Mango, name = "Mango"),
    path('Watermelon/', views.Watermelon, name = "Watermelon"),
    path('Banana/', views.Banana, name = "Banana"),
    path('Apple/', views.Apple, name = "Apple"),
    path('Guava/', views.Guava, name = "Guava"),
    path('Grapes/', views.Grapes, name = "Grapes"),
    path('Orange/', views.Orange, name = "Orange"),
    path('Lemon/', views.Lemon, name = "Lemon"),
    path('Broccoli/', views.Broccoli, name = "Broccoli"),
    path('Lettuce/', views.Lettuce, name = "Lettuce"),
    path('Carrots/', views.Carrots, name = "Carrots"),
    path('Potato/', views.Potato, name = "Potato"),
    path('Cucumber/', views.Cucumber, name = "Cucumber"),
    path('Tomato/', views.Tomato, name = "Tomato"),
    path('Garlic/', views.Garlic, name = "Garlic"),
    path('Onion/', views.Onion, name = "Onion"),
    path('SourdoughBread/', views.SourdoughBread, name = "SourdoughBread"),
    path('PeanutButter/', views.PeanutButter, name = "PeanutButter"),
    path('Pickles/', views.Pickles, name = "Pickles"),
    path('Sugar/', views.Sugar, name = "Sugar"),
    path('Cheerios/', views.Cheerios, name = "Cheerios"),
    path('BrownRice/', views.BrownRice, name = "BrownRice"),
    path('CannedBeans/', views.CannedBeans, name = "CannedBeans"),
    path('Oreos/', views.Oreos, name = "Oreos"),
    #Dynamic product pages
    path('product/<str:pk>',views.dynamic_product_pages)




]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
