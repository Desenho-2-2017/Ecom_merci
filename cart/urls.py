from django.conf.urls import url
from cart.views import cartDetailView, removeFromCartView


urlpatterns = [
    url(r'^cart_detail/', cartDetailView, name='cartDetailView'),
    url(r'^(?P<product_id>[0-9]+)/remove_from_cart/$', removeFromCartView,
        name='removeProductFromCart')
]
