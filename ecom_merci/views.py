from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    http_method_names = [u'get']

    def get(self, request):
        response = render(request, 'home.html')
        return response
