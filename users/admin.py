
from django.contrib import admin
from .models import ShippingAddress, CustomerUser, PhoneNumber, CreditCard

admin.site.register(ShippingAddress)
admin.site.register(CustomerUser)
admin.site.register(PhoneNumber)
admin.site.register(CreditCard)
