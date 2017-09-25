from django.shortcuts import render
from django.http import HttpResponse
from .models import (ProductCategory, Product)


def productIndexView(request):

    queryset = Product.objects.all()
    context = {
        "products": queryset,
    }

    return render(request, "productIndex.html", context)
