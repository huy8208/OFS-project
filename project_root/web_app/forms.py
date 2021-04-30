from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Customer

class CreateCustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = Customer  #Tell form to use Customer model
        fields = ("email","username","password1","password2")