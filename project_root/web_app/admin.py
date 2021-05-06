from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Configure setting for localhost:8000/admin

from .models import *

class CustomerAdmin(UserAdmin):
    list_display = ('id','email','username','date_created', 'last_login', 'is_customer', 'is_admin','is_staff')
    search_fields = ('email','username',)
    readonly_fields=('date_created', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','category','slug','description','date_created','image','amount_in_stock')
    ordering = ('id',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id','customer','address','city','state','zipcode')

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(OrderedItem)
admin.site.register(ShippingAddress,AddressAdmin)