from django.shortcuts import render
from django.http import Http404
from .models import (ProductCategory, Product)


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
