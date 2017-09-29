from django.shortcuts import render
from django.views.generic import View

# This code is just for testing only and will be deleted.
class FrontView (View):
    http_method_names = [u'get', u'post']

    def get(self,request):
        return render(request,'homepage.html')
