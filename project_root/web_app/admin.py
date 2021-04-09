from django.contrib import admin

# Configure setting for localhost:8000/admin

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)