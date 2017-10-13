# from django.shortcuts import render
from django.shortcuts import render_to_response
from cart.cart import Cart
from products.models import Product
from django.views.generic import View


class CartManagement(View):

    def addToCart(request, product_id, quantity):
        product = Product.objects.get(id=product_id)
        cart = Cart(request)
        cart.add(product, product.unit_price, quantity)

    def removeFromCart(request, product_id):
        product = Product.objects.get(id=product_id)
        cart = Cart(request)
        cart.remove(product)


def cartDetailView(request):
    return render_to_response('cartDetail.html', dict(cart=Cart(request)))
