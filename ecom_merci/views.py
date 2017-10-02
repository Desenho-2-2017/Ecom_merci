from django.shortcuts import render
from django.views.generic import View
from products.models import Product


class HomeView(View):
    http_method_names = [u'get']

    def get(self, request):
        response = render(request, 'home.html')
        return response


def renderAdvertisements(request):
    queryset = Product.objects.all()
    context = {
        "products": queryset,
    }

    return render(request, "home.html", context)
