from cart.cart import Cart
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from products.models import Product


class CartManagement(View):

    def addToCart(request, product_id, quantity):
        product = Product.objects.get(id=product_id)
        cart = Cart(request)
        cart.add(product, product.price, quantity)

    @csrf_exempt
    def removeFromCart(request, product_id):
        product = Product.objects.get(id=product_id)
        cart = Cart(request)
        cart.remove(product)


def cartDetailView(request):
    return render_to_response('cartDetail.html', dict(cart=Cart(request)))


@csrf_exempt
def removeFromCartView(request, product_id):

    CartManagement.removeFromCart(request, product_id)

    return redirect('/cart/cart_detail')
