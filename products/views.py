from django.shortcuts import render
# from django.http import HttpResponse
from .models import Product
from django.http import Http404


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
