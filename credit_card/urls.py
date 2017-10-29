from django.conf.urls import url
from .apps import CreditCardConfig
from credit_card.views import CreditCardDetailView



urlpatterns = [
    url(r'^credit_card/', CreditCardDetailView, name='credit_card'),
    # url(r'^(?P<product_id>[0-9]+)/remove_from_cart/$', removeFromCartView,
    #     name='removeProductFromCart')
]
