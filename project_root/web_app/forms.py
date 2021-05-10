from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Customer,ShippingAddress
# from django_countries.fields import CountryField
# from django_countries.widgets import CountrySelectWidget
class CreateCustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = Customer  #Tell form to use Customer model
        fields = ("email","username","password1","password2")

class CreateShippingAddressForm(forms.ModelForm):
    class Meta:
        model=ShippingAddress
        fields = ("address","zipcode","state","city")


