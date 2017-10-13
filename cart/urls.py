from django.conf.urls import url
from cart.views import (CartManagement,
                        cartDetailView)

urlpatterns = [
    url(r'^cart_detail/', cartDetailView, name='cartDetailView'),
]
