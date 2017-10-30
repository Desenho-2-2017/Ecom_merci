from cart.views import cartDetailView, removeFromCartView
from django.conf.urls import url
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^cart_detail/', login_required(cartDetailView),
        name='cartDetailView'),
    url(r'^(?P<product_id>[0-9]+)/remove_from_cart/$',
        login_required(removeFromCartView),
        name='removeProductFromCart')
]
