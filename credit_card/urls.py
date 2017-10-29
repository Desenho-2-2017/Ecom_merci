from django.conf.urls import url
from credit_card.views import CreditCardDetailView

urlpatterns = [
    url(r'^checkout/', CreditCardDetailView, name='creditCardView')
    # url(r'^(?P<product_id>[0-9]+)/remove_from_cart/$', removeFromCartView,
    #     name='removeProductFromCart')
]
