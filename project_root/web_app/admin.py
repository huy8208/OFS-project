from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Configure setting for localhost:8000/admin

from .models import *

class CustomerAdmin(UserAdmin):
    list_display = ('email','username','date_created', 'last_login', 'is_admin','is_staff')
    search_fields = ('email','username',)
    readonly_fields=('date_created', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)