from django.contrib import admin
from .models import ShippingAddress, CustomerUser, CreditCard

admin.site.register(ShippingAddress)
admin.site.register(CustomerUser)
admin.site.register(CreditCard)
