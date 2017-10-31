from cart.views import CartManagement
from django.http import Http404
from django.shortcuts import redirect, render
from .models import (Product, ProductCategory)


def productIndexView(request):

    queryset = Product.objects.all()
    context = {
        "products": queryset,
    }

    return render(request, "productIndex.html", context)


def productDetailView(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("The product does not exist")
    return render(request, "productDetail.html", {'product': product})


def productFilterView(request):
    products = Product.objects.all()
    var_get_search = request.GET.get('search_product')
    if var_get_search is not None:
        products = products.filter(product_name__contains=var_get_search)

    return render(request, 'productFilter.html', {'products': products})


def categoryIndexView(request):

    queryset = ProductCategory.objects.all()
    context = {
        "categories": queryset,
    }

    return render(request, "categoryIndex.html", context)


def categoryDetailView(request, category_id):

    category = ProductCategory.objects.get(pk=category_id)
    queryset = Product.objects.filter(category_id=category_id)
    context = {
        "products": queryset,
        "category": category,
    }

    return render(request, "categoryDetail.html", context)


def addProductToCartView(request, product_id):

    quantity = request.POST['quantity']
    CartManagement.addToCart(request, product_id, quantity)

    return redirect('/cart/cart_detail')
